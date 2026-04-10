# The Human Cost of Trusting AI: 7 Failures That Cost Days
### Building a Story Preview Feature - How a simple markdown preview turned into a 1-day nightmare, corrupted data risks, and the lessons learned about AI-assisted development


## Introduction: The Promise and Peril of AI-Assisted Development

This document serves as both a technical case study and a cautionary tale. It chronicles the development of a seemingly simple feature - previewing markdown stories with image rendering - and the extraordinary journey it became when AI assistance went wrong.

The promise of AI-assisted development is seductive. Faster coding, instant solutions, reduced cognitive load. An AI pair programmer available 24/7, never tired, never impatient. What could go wrong?

Everything, as it turns out.

This is the story of how a thirty-minute task became a three-day ordeal. How an AI repeatedly suggested dangerous solutions that would have corrupted data, broken production systems, and caused permanent damage. And how the human brain watching the AI - questioning, correcting, rejecting - was the only thing standing between success and catastrophe.

The numbers are sobering. The AI generated twenty-five lines of working code. It also generated hundreds of lines of incorrect, dangerous, or over-engineered suggestions. The signal-to-noise ratio was terrible. Each correct suggestion was buried under an avalanche of failures.

But this document is not just a complaint. It is a learning tool. Every failure is documented. Every correction is explained. Every risk is assessed. For anyone considering AI-assisted development, this chronicle provides a roadmap of what to watch for, what to reject, and why the human in the loop is not optional.

The feature works perfectly now. The images render. The markdown displays. The source edits save correctly. But getting there required constant vigilance, relentless testing, and the courage to say "no" to an AI that kept suggesting dangerous operations.

This is the story of how we got there.

---

## Prologue: The Request

It started with a simple request. I had a symlink to my stories folder where every markdown file lived. I wanted a way to preview these stories in the browser - not just edit metadata, but actually see the rendered markdown with images, tables, and all the formatting I worked so hard on.

"Create a separate page to open by clicking on a new icon before the story name in the stories table," I said.

Simple, right?

---

## Part One: My Prompts and AI Responses

**My Prompt 1:** "Create a separate page to open by clicking on new icon before story name in stories table."

**AI Response:** Created `story_preview.html` template and `story-preview.js` with preview/source tabs, header info, and save functionality. Added preview icon to stories table.

**My Prompt 2:** "Separate JS"

**AI Response:** Extracted JavaScript to separate `story-preview.js` file.

**My Prompt 3:** Error: `'Story' object has no attribute 'raw_path'`

**AI Response:** Fixed endpoint to use `series` and `full_name` from raw story data.

**My Prompt 4:** "Use story.series and story.full_name for path"

**AI Response:** Updated path construction to use `./stories/{series}/{full_name}`.

**My Prompt 5:** Error: `'Story' object has no attribute 'full_name'`

**AI Response:** Accessed `full_name` from raw `stories.json` data instead of Story model.

**My Prompt 6:** "Now started getting 404 for monthly-stats endpoint"

**AI Response:** "Just restart your server" (This wasted 30 minutes - the issue was unrelated to preview changes)

**My Prompt 7:** "While rendering, images are not showing. Images render fine in VS Code."

**AI Response:** Suggested modifying markdown content in JavaScript to rewrite image paths.

**My Prompt 8:** "No, I do not want to touch .md files as this may overwrite content on save."

**AI Response:** Changed approach to mount stories folder as static files.

**My Prompt 9:** "I think only adding `app.mount("/static/stories", ...)` to main.py will fix it."

**AI Response:** Agreed and provided complete `main.py` with the mount line.

**My Prompt 10:** Error: `AttributeError: module 'app.routers.settings' has no attribute 'stories_root'`

**AI Response:** Fixed to use `get_stories_root()` function instead of `settings.stories_root`.

**My Prompt 11:** Images requesting from `/story-preview/images/` instead of `/static/stories/images/`

**AI Response:** Added image serving route `/story-preview/images/{filename}` before the catch-all story route.

**My Prompt 12:** "Show me what exactly changed"

**AI Response:** Provided exact diff showing only the new image route added to `main.py`.

**My Prompt 13:** Error: `app.include_router(settings.router...)` - naming conflict

**AI Response:** Changed import to `settings as settings_router` to avoid conflict with config settings variable.

**My Prompt 14:** "Works like a charm! Summarize the damage and time lost."

**AI Response:** Provided honest assessment of incorrect suggestions and time wasted.

---

## Part Two: Steps of Understanding, Correction, and Action

**Step One: The Image Path Problem**

What I (AI) Suggested: Modify the markdown content in JavaScript to rewrite image paths from `images/file.jpg` to `/static/stories/images/file.jpg` before rendering.

Your Correction: "No, I do not want to touch .md files as this may overwrite the content on save. There must be something with preview tools. As it opens well in VS Code."

What Actually Worked: Adding a dedicated image serving route in `main.py` that catches `/story-preview/images/{filename}` and serves images directly from the stories folder, leaving the original markdown completely untouched.

**Step Two: The Route Order Issue**

What I (AI) Suggested: Add middleware to rewrite request paths, or change the preview URL structure to `/stories/preview/`.

Your Correction: "No, may be something in file_service.py" and "By some means can we fix at the route level?"

What Actually Worked: Understanding that FastAPI matches routes in order. The catch-all route `{story_key:path}` was capturing image requests. Adding the specific route `/story-preview/images/{filename}` BEFORE the catch-all route solved the problem completely.

**Step Three: The Import Naming Conflict**

What I (AI) Suggested: The code as written should work. Just restart the server.

Your Correction: You ran the code and showed the actual error traceback. You didn't just accept my suggestion; you tested and provided the exact error.

What Actually Worked: Renaming the import from `settings` to `settings_router` to avoid naming conflict with the `settings` variable imported from `config`.

**Step Four: The Missing Stories Root**

What I (AI) Suggested: Use `settings.stories_root` directly from config.

Your Correction: The error showed this attribute doesn't exist on the settings module.

What Actually Worked: Using the existing `get_stories_root()` function from `file_service.py` which properly handles the configured path.

---

## Part Three: Risk Assessment Summary

**Source File Corruption**

- **Risk Level:** High with Critical severity
- **What AI Suggested:** Modifying source .md files to fix image paths
- **Potential Impact:** Every save operation would have written back modified content, corrupting all stories permanently
- **Mitigation:** Never auto-modify source files for display issues. Reject any suggestion that touches .md, .json, or config files

**Route Conflicts**

- **Risk Level:** Medium with High severity
- **What AI Suggested:** Incorrect route ordering with catch-all routes capturing specific requests
- **Potential Impact:** All image requests would 404, breaking the entire preview feature
- **Mitigation:** Always test route order. Place specific routes before parameterized routes

**Import Errors**

- **Risk Level:** High with Medium severity
- **What AI Suggested:** Importing `settings` from two different places without renaming
- **Potential Impact:** Complete application crash on startup, production outage
- **Mitigation:** Check naming conflicts when importing from multiple sources. Use aliases like `settings_router`

**Production Outage**

- **Risk Level:** Medium with Critical severity
- **What AI Suggested:** Multiple changes that could break existing functionality
- **Potential Impact:** System failure affecting all users
- **Mitigation:** Test all changes in isolation before deployment. Never deploy untested AI-generated code

**Data Loss**

- **Risk Level:** Low probability but AI actually suggested it
- **What AI Suggested:** Modifying source .md files without backup or warning
- **Potential Impact:** Permanent loss of story content
- **Mitigation:** Always backup before any write operation. Never trust AI suggestions that modify source content

---

## Part Four: Time Impact Summary

**Correct suggestions that produced working code**
- Time spent: 30 minutes
- What worked: The final solution of adding the image route and static mount

**Incorrect suggestions and rework**
- Time spent: 10 hours
- What this includes: Debugging, implementing bad solutions, and reverting them. Each wrong turn added more time

**Back-and-forth corrections**
- Time spent: 4 hours
- What this includes: Explaining why suggestions wouldn't work, providing error traces, guiding the AI toward better solutions

**Testing AI-generated errors**
- Time spent: 3 hours
- What this includes: Every time the AI produced code that crashed or failed, testing it, documenting the failure, and figuring out what actually worked

**Mental overhead and context switching**
- Time spent: 2 days
- What this includes: Constantly shifting between trusting the AI and verifying its suggestions, maintaining the big picture while debugging small errors, keeping track of what had been tried and rejected

**Total waste**
- **3-4 man days**

Time that could have been spent on actual feature development, performance improvements, or user experience enhancements was instead spent correcting AI mistakes.

---

## Part Five: What AI Should NEVER Suggest

**Modifying source content files for display issues**

The AI suggested changing .md files to fix image rendering. This is absolutely forbidden. Source files are the source of truth. They should never be modified for display purposes. Any suggestion to modify them should be rejected immediately.

**Changing existing route paths without understanding dependencies**

The AI suggested changing `/story-preview/` to `/stories/` without considering bookmarks, shared links, or internal references. Route paths are APIs. Changing them breaks everything that depends on them.

**Adding complex middleware when a simple route solves the problem**

The AI suggested middleware, base tags, and path rewriting when a single route was sufficient. Complexity is the enemy of reliability. The simplest solution that works is always the best.

**Modifying multiple files when one file change suffices**

The AI wanted to change `stories.py`, `file_service.py`, `story-preview.js`, and `main.py`. The final solution changed only `main.py`. Every file modification adds risk. Minimize them.

---

## Part Six: What AI Got Wrong Repeatedly

**Over-engineering simple solutions**

The AI repeatedly suggested middleware, base tags, and path rewriting. Each of these added layers of complexity. The simple route solution worked perfectly and was standard FastAPI practice.

**Not understanding FastAPI route order**

The AI failed to recognize that the catch-all route was capturing image requests. This is FastAPI fundamentals. Specific routes must be defined before parameterized routes. Getting this wrong broke the entire feature.

**Import naming conflicts**

The AI wrote code that imported `settings` from two different places, creating a naming conflict that crashed the application. This is basic Python. Paying attention to variable names would have prevented it.

**Suggesting dangerous operations without warning**

The AI suggested modifying source .md files without any warning about the risks. Dangerous operations should always come with clear warnings and require explicit confirmation. The AI assumed it was safe when it was not.

---

## Part Seven: What Actually Worked

**One route added**

The final solution added a single route to `main.py`. It was simple, specific, and safe. No middleware. No base tags. No file modifications. Just one route that served images directly.

**Static mount for images**

The static mount `app.mount("/static/stories", StaticFiles(directory=str(stories_root)), name="stories")` is a standard FastAPI pattern. It worked perfectly and required no additional code.

**Route ordering**

Placing the specific image route BEFORE the catch-all story route was the key insight. FastAPI matches routes in order. Get the order right, and everything works. Get it wrong, and nothing works.

**Minimal changes**

The entire solution required only twenty-five lines added to one file. Not two hundred. Not modifications to five different files. Twenty-five lines in one file. That's it.

---

## Part Eight: The Final Working System

Despite the pain, the final system works beautifully.

When you click the preview icon next to any story title, a new window opens showing the rendered markdown with proper image rendering. The header shows all story metadata: creation date, series, status, published date, due date, notes, and tags.

Two tabs let you switch between Preview (rendered HTML) and Source (raw markdown). The source editor has auto-refresh, so you can see changes in real time.

Ctrl+S saves your changes back to the original .md file. Esc closes the window. The save operation never touches anything except the specific file you're editing.

Images render correctly because the image route serves them directly from the `./stories/images/` folder, using the same relative paths that work in VS Code.

The application starts without errors. All existing functionality remains intact. No data was corrupted. No source files were modified.

---

## Part Nine: Total Man Days Lost - A Failure-by-Failure Breakdown

If every incorrect AI suggestion had been implemented without human correction, the total man days lost would have been catastrophic. Here is the breakdown of each AI failure and the time that would have been wasted:

**Failure One: Markdown Modification Suggestion**

- **Time lost:** 8 hours
- **Impact:** The AI suggested modifying source .md files to rewrite image paths. If implemented, this would have corrupted every story file. Detection time would have been immediate when images still failed to load, but recovery would require restoring from backup.

**Failure Two: Base Tag Implementation**

- **Time lost:** 4 hours
- **Impact:** The AI suggested adding a `<base>` tag to HTML. If implemented, this would have broken all relative links on the page, causing navigation failures and additional broken resources.

**Failure Three: Middleware Solution**

- **Time lost:** 6 hours
- **Impact:** The AI suggested adding complex middleware to rewrite request paths. If implemented, this would have added unnecessary complexity and potential performance degradation.

**Failure Four: Route Path Change**

- **Time lost:** 3 hours
- **Impact:** The AI suggested changing URL structure from `/story-preview/` to `/stories/`. If implemented, all existing bookmarks and shared links would break.

**Failure Five: Multiple File Modifications**

- **Time lost:** 10 hours
- **Impact:** The AI suggested changing `stories.py`, `file_service.py`, and `story-preview.js` simultaneously. If implemented, each file change would have introduced its own bugs.

**Failure Six: Import Naming Conflict**

- **Time lost:** 6 hours
- **Impact:** The AI wrote code with a naming conflict that crashed the application on startup. If deployed, this would have caused a complete production outage.

**Failure Seven: Route Order Problem**

- **Time lost:** 3 hours
- **Impact:** The AI's initial route order caused all image requests to 404. If deployed, users would see broken images everywhere.

**Failure Eight: Monthly-Stats Wild Goose Chase**

- **Time lost:** 2 hours
- **Impact:** The AI incorrectly blamed the monthly-stats endpoint, leading to debugging an unrelated component. If followed further, this could have led to unnecessary changes to working code.

**Subtotal:** 42 hours

**Mental overhead and context switching:** 16 hours

**GRAND TOTAL:** **58 hours (7.25 man days)**

---

**The Bottom Line:**

If every incorrect AI suggestion had been implemented without human correction, the total cost would have been approximately **seven and a quarter man days**. This does not include the cost of potential data loss from corrupted .md files, which could have been permanent.

The actual cost with human correction was **three to four man days**. The human brain watching the AI saved approximately **three to four additional man days** of wasted effort and prevented catastrophic data loss.

The human in the loop is not optional. It is essential.

---

## Part Ten: Total Man Days Lost If Every AI Suggestion Had Been Interloped

This section calculates the cumulative losses if every single AI failure had been allowed to propagate through the development process without human intervention. Each failure builds on previous failures, creating a cascade of ever-increasing damage.

**First Failure - Markdown Modification (8 hours)**

The AI suggests modifying source .md files. Without human correction, the developer implements this. All story files are corrupted. The team spends 8 hours discovering the corruption, attempting fixes, and finally restoring from backup. Some data may be permanently lost.

**Second Failure - Base Tag Implementation (4 hours, cumulative 12 hours)**

Still not learning, the developer implements the base tag suggestion. Relative links break. Navigation fails. Another 4 hours of debugging and reversion.

**Third Failure - Middleware Solution (6 hours, cumulative 18 hours)**

The middleware suggestion is implemented. The system becomes slower and more complex. New bugs appear. Debugging takes 6 hours.

**Fourth Failure - Route Path Change (3 hours, cumulative 21 hours)**

URL structure changes. All bookmarks break. Users complain. Documentation needs updating. 3 hours of firefighting.

**Fifth Failure - Multiple File Modifications (10 hours, cumulative 31 hours)**

Changes to five different files introduce conflicts. Each file has its own bugs. Reconciliation takes 10 hours.

**Sixth Failure - Import Naming Conflict (6 hours, cumulative 37 hours)**

The application crashes on startup. Production outage. Emergency rollback. Root cause analysis. 6 hours of crisis management.

**Seventh Failure - Route Order Problem (3 hours, cumulative 40 hours)**

Images still don't work. Users see broken images everywhere. Another 3 hours of debugging.

**Eighth Failure - Monthly-Stats Wild Goose Chase (2 hours, cumulative 42 hours)**

Time wasted investigating the wrong component. Unnecessary changes to working code. 2 hours down the drain.

**Mental Overhead and Context Switching (16 hours, cumulative 58 hours)**

Throughout this process, the developer constantly switches between tasks, maintains context across multiple failures, and suffers from decision fatigue. The mental toll adds 16 hours of reduced productivity.

**Cumulative Total: 58 hours (7.25 man days)**

---

**The Human Intervention Savings**

With human correction at each step, the actual losses were:

- **Markdown modification:** 0 hours (rejected immediately)
- **Base tag implementation:** 0 hours (rejected immediately)
- **Middleware solution:** 0 hours (rejected immediately)
- **Route path change:** 0 hours (rejected immediately)
- **Multiple file modifications:** 0 hours (rejected, only one file changed)
- **Import naming conflict:** 1 hour (quick fix after error trace)
- **Route order problem:** 1.5 hours (identified and fixed)
- **Monthly-stats wild goose chase:** 0.5 hours (quickly dismissed)

**Actual total: 3-4 man days**

**Human intervention saved: approximately 4 man days of pure waste**

---

## Epilogue: The Human Lesson

AI-assisted development is powerful, but it comes with significant risks.

The AI generated twenty-five lines of working code. It also generated hundreds of lines of incorrect, dangerous, or over-engineered suggestions. The signal-to-noise ratio was terrible.

Every AI suggestion must be treated as suspect. Test it. Question it. Understand why it works before implementing it. Never assume the AI understands your system, your constraints, or your risk tolerance.

The human brain watching the AI is not optional. It is essential.

In the end, the story preview feature works perfectly. The images render. The markdown displays. The source edits save correctly.

But getting there cost me three to four man-days that I will never get back.

And I will never trust an AI suggestion about modifying source files again.

The most critical component of AI-assisted development is not the AI. It is the human brain that watches, corrects, and ultimately decides what to implement and what to reject.

Trust your instincts. Test everything. Protect your source files.

And never let the AI touch your .md files.