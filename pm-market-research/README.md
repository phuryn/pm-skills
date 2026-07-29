# pm-market-research

Market research skills for PMs: user personas, segmentation, sentiment analysis, X social listening with Xquik, and competitive analysis.

## Skills (7)

- **competitor-analysis** — Analyze competitors with strengths, weaknesses, and differentiation opportunities.
- **customer-journey-map** — Create an end-to-end customer journey map with stages, touchpoints, emotions, pain points, and opportunities.
- **market-segments** — Identify 3-5 potential customer segments with demographics, JTBD, and product fit analysis.
- **market-sizing** — Estimate market size using TAM, SAM, and SOM with top-down and bottom-up approaches.
- **sentiment-analysis** — Analyze feedback and X social-listening data with traceable sentiment, themes, and segment insights.
- **user-personas** — Create refined user personas from research data.
- **user-segmentation** — Segment users from feedback data based on behavior, JTBD, and needs.

## Commands (3)

- `/pm-market-research:analyze-feedback` — Analyze feedback or a bounded Xquik sample with sentiment, themes, and segment insights.
- `/pm-market-research:competitive-analysis` — Analyze the competitive landscape — identify competitors, compare strengths and weaknesses, find differentiation opportunities.
- `/pm-market-research:research-users` — Comprehensive user research — build personas, segment users, and map the customer journey from research data.

## X Social Listening With Xquik

Use `/pm-market-research:analyze-feedback` for current public X research.

Provide a research question, search query, time window, ordering, and sample
limit. The workflow uses a configured Xquik MCP connection when available. It
can also use REST when `XQUIK_API_KEY` already exists in the environment.

Example:

```text
/pm-market-research:analyze-feedback Research onboarding complaints on X.
Search "product onboarding" from 2026-07-01 through 2026-07-08.
Collect up to 100 Latest posts with Xquik.
```

The workflow preserves source URLs and collection metadata. It deduplicates
posts, labels sampling bias, and separates evidence from interpretation.

See the [Xquik REST overview](https://docs.xquik.com/api-reference/overview) and
[MCP setup](https://docs.xquik.com/mcp/overview).

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
