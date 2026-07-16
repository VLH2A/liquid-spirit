CLAUDE.md — Wine & Spirits Menu Analyzer (demo)

What this is

A throwaway proof-of-concept. A sales rep photographs a drinks menu, Claude vision reads it, we compare against a William Grant & Sons knowledge base, and return sales intelligence. Streamlit frontend, Python pipeline, one JSON knowledge base. No database, no auth, no deploy, no persistence. Everything runs per-session.

Goal is a demo that makes a William Grant contact want a pilot. Not production. Not polished. It just has to work and sound like a spirits person.

How we work


Contracts before code. Before writing a slice, state its goal, inputs, outputs, and what done looks like. Keep it to a few lines. No ceremony.
One slice at a time. Minimal diff. I give you an explicit list of files you may touch. Don't touch anything else.
Stop when unsure. If a business rule, schema, or source is missing or ambiguous, STOP and ask. Never invent.
I write the knowledge base content and the analysis prompt myself. You handle scaffolding, the pipeline glue, and the Streamlit wrapper. Don't write KB content or market claims.


Never do


Never state a market claim (market share, "fastest-growing", "highest-performing", sales figures) that isn't traceable to a public source in the knowledge base. If it isn't sourced, soften it or leave it out. This is the single most important rule in the project.
Never hallucinate brands onto a menu that aren't there. If the photo is unclear or partial, say so in the output.
Never invent WG&S product facts. Product data comes from the knowledge base only.
No database, no auth, no user accounts, no CRM anything. If a task seems to need one, stop and ask.
No drive-by refactors. Change only the files listed for the current slice.


Stack

Python, Streamlit, Kilo gateway (OpenAI-compatible — vision for menu reading, text for analysis), one JSON knowledge base. Gateway base URL / key / model in .env, never in code, never in the bundle.