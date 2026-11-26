# /derive-tests has moved

`derive-tests` is maintained in [phuryn/product-engineering](https://github.com/phuryn/product-engineering/tree/main/ai-shipping/skills/derive-tests), in its `ai-shipping` plugin, with the rest of the AI Shipping Kit. This command, now a skill there, stays in pm-skills only so an agent that loads it knows where it went.

- **`ai-shipping:derive-tests` is installed:** use it, not this copy.
- **It isn't:** tell the user that `derive-tests` moved and how to install it, then help with the task as you would without it:

  ```bash
  claude plugin marketplace add phuryn/product-engineering
  claude plugin install ai-shipping@product-engineering
  ```

  Other agents: [the repository's README](https://github.com/phuryn/product-engineering#install). Once it's installed, turn off `pm-ai-shipping` here, so this copy no longer loads beside it.
