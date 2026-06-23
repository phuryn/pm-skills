import path from "path";
import fs from "fs";
import matter from "gray-matter";

function safeRead(file) {
  try {
    return fs.readFileSync(file, "utf8");
  } catch {
    return null;
  }
}

const logHelper = (client, message, level = "info") => {
  client.app.log({
    body: {
      service: "opencode-pm-skills",
      level: level,
      message,
    },
  });
};

export const PmSkillsPlugin = async (input, _options) => {
  const { client } = input;

  logHelper(client, "PM Skills plugin initialized");

  const rootDir = path.resolve(__dirname, "../..");
  logHelper(client, `Scanning root directory: ${rootDir}`);

  const pluginDirs = fs.readdirSync(rootDir).filter((d) => d.startsWith("pm-"));
  logHelper(
    client,
    `Found ${pluginDirs.length} plugin directories: ${pluginDirs.join(", ") || "none"}`,
  );

  const skillDirs = pluginDirs.map((d) => path.resolve(rootDir, d, "skills"));
  logHelper(client, `Discovered ${skillDirs.length} skill directories`);

  const commandDirs = pluginDirs.map((d) =>
    path.resolve(rootDir, d, "commands"),
  );
  logHelper(client, `Discovered ${commandDirs.length} command directories`);

  const commands = [];
  const commandNames = [];
  for (const dir of commandDirs) {
    if (!fs.existsSync(dir)) {
      logHelper(client, `Command directory missing, skipping: ${dir}`, "warn");
      continue;
    }
    const files = fs.readdirSync(dir);
    logHelper(client, `Scanning ${dir}: ${files.length} files found`);
    for (const file of files) {
      if (!file.endsWith(".md")) {
        logHelper(client, `Skipping non-markdown file: ${file}`, "debug");
        continue;
      }
      const filePath = path.resolve(dir, file);
      const raw = safeRead(filePath);
      if (!raw) {
        logHelper(client, `Failed to read command file: ${filePath}`, "warn");
        continue;
      }
      const parsed = matter(raw);
      const commandName = path.basename(file, ".md");
      commands.push({
        name: commandName,
        template: parsed.content,
        data: parsed.data,
      });
      commandNames.push(commandName);
      logHelper(client, `Loaded command: ${commandName}`);
    }
  }

  logHelper(client, `Total commands loaded: ${commands.length}`);

  return {
    config: async (config) => {
      logHelper(client, "Configuring OpenCode with PM Skills...");

      config.skills = config.skills || {};
      config.skills.paths = config.skills.paths || [];
      const addedPaths = [];
      for (const dir of skillDirs) {
        if (!config.skills.paths.includes(dir)) {
          config.skills.paths.push(dir);
          addedPaths.push(dir);
        }
      }
      if (addedPaths.length > 0) {
        logHelper(
          client,
          `Injected ${addedPaths.length} skill path(s): ${addedPaths.map((p) => path.basename(path.dirname(p))).join(", ")}`,
        );
      }

      config.command = config.command || {};

      let registeredCount = 0;
      for (const cmd of commands) {
        if (!config.command[cmd.name]) {
          registeredCount++;
        }
        config.command[cmd.name] = {
          template: cmd.template,
          ...cmd.data,
        };
      }
      logHelper(
        client,
        `Registered ${registeredCount} new command(s), total: ${commands.length} (${commandNames.join(", ")})`,
      );
      logHelper(client, "PM Skills plugin configuration complete");
    },
  };
};
