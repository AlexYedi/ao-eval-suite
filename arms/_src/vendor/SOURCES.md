# Outside skills used as arms D and F

Copied byte for byte at the commits below on 2026-11-14. The sha256 of each copy is frozen in `prereg/HASHES.json` at sign.

## Arm D: `social`, from coreyhaines31/marketingskills

- File: `skills/social/SKILL.md`. Used as published: SKILL.md only. Its nine reference files load only on demand, and the sampling recipe gives the model no tools to load them.
- Commit: `1f837447b20bb6f0e72d87b80ece1c221c362c7d`
- Licence: MIT, Copyright (c) 2025 Corey Haines. Full text in `D-LICENSE`.
- Size: 2,800 words.
- Chosen because it was the most-used GTM writing skill with a confirmed permissive licence (about 60k stars) whose SKILL.md stands on its own. It covers several platforms, not just LinkedIn, and sends outreach to a separate cold-email skill, so it gives little DM-specific guidance (types T5, T7 and T8). It is tested as published, on tasks it did not choose.
- Runners-up: sergebulaev/linkedin-skills `linkedin-post-writer` at `8f8bc4b`, MIT (its references are stubs that depend on other files), and charlie947/social-media-skills `post-writer` at `10ca79c`, MIT (it stops without the user's voice files).

## Arm F: `elements-of-style`, from the Superpowers marketplace

- Marketplace entry: obra/superpowers-marketplace, plugin `elements-of-style` v1.0.0, which points to obra/the-elements-of-style.
- Files: `skills/writing-clearly-and-concisely/SKILL.md` (325 words, newly written) followed by `skills/writing-clearly-and-concisely/elements-of-style.md` (12,154 words; Strunk's 1918 text from Project Gutenberg #37134 converted to markdown).
- Commit: `05fc4f0d2b97b7c042dd9949ad658568e4a1324e`
- Licence: the Strunk text is public domain. The repo has no LICENSE file. Its `package.json` (copied as `F-package.json`) declares `"license": "Public Domain"`, which this study takes as the author's dedication of the SKILL.md wrapper.
- Fallback named in PREREG.md section 6, if that is judged not to be a confirmed licence: the Gutenberg #37134 text alone.

## Prompt length

Arm D adds about 2,800 words of guidance and arm F about 12,500. Arms B and C add under 150. Guidance length therefore varies with arm. Input tokens are recorded for every sample, and the results report them per arm.
