# The Human Cost of Trusting AI: 8 Hours of Hell
### Building a Story Edit Feature - How a simple modal turned into an 8-hour nightmare, destroyed architecture, and why AI can't follow context even when you beat it over the head with it

![Experience/images/The Human Cost of Trusting AI: 8 Hours of Hell](<images/The Human Cost of Trusting AI: 8 Hours of Hell.png>)
# Introduction: The Promise and Peril of AI-Assisted Development

This document serves as both a technical post-mortem and a cautionary tale. It chronicles the development of a story edit feature - a seemingly straightforward task of adding a modal popup to edit story metadata - and the extraordinary journey it became when AI assistance went wrong.

The promise of AI-assisted development is seductive. Faster coding, instant solutions, reduced cognitive load. An AI pair programmer available 24/7, never tired, never impatient. What could go wrong?

Everything, as it turns out.

This is the story of how a two-hour task became a seven-hour ordeal. How an AI repeatedly suggested dangerous solutions that would have broken production systems, corrupted architectural patterns, and caused permanent damage. And how the human brain watching the AI - questioning, correcting, rejecting - was the only thing standing between success and catastrophe.

The numbers are sobering. The AI generated approximately two hundred lines of working code. It also generated approximately five hundred lines of incorrect, dangerous, or over-engineered suggestions. The signal-to-noise ratio was terrible. Each correct suggestion was buried under an avalanche of failures.

But this document is not just a complaint. It is a learning tool. Every failure is documented. Every correction is explained. Every risk is assessed. For anyone considering AI-assisted development, this chronicle provides a roadmap of what to watch for, what to reject, and why the human in the loop is not optional.

The feature works perfectly now. The modal opens. The data loads. The saves complete. The monthly stats display correctly.

But getting there required constant vigilance, relentless testing, and the courage to say "no" to an AI that kept suggesting dangerous operations.

This is the story of how we got there.

---

## Part One: The Original Ask

I needed to discard the existing Story Edit functionality and build it from scratch with three specific sections:

**Section 1:** All story metadata editable with icons - including notes, series dropdown using existing endpoints.

**Section 2:** LinkedIn marketing fields - status, timestamp, impressions, URL, post type.

**Section 3:** Non-editable Medium statistics - top-level metadata (ID, unique slug, first published, publication, responses, read time in hh:mm format, word count, last update, votes, claps) plus a monthly stats table showing period, views, reads, and earnings with month dropdown and sync button that refreshes the entire page.

The requirements were clear. No HTML in JavaScript. Keep HTML and JS separate. Use story.name as the identifier, not uniqueSlug.

This was supposed to be a straightforward task. It turned into a multi-day ordeal.

---

## Part Two: The Initial Disaster - Opening the Modal

### My Prompt to AI

"Discard the existing Story Edit functionality. And start from scratch. Based on Story model, create following sections... No code, with your understanding."

### AI Response - First Mistake

The AI provided a detailed mapping and structure diagram. It correctly identified fields, sections, and the need for story.name normalization. But when it came time to generate actual code, everything went wrong.

The AI created edit-story.js with an IIFE wrapper to avoid global conflicts. It set up the modal HTML correctly. But the openEditStory function used uniqueSlug as the identifier.

### What Went Wrong

When I clicked the story title, nothing happened. No error in browser console. No error in Python console. The modal simply would not open.

The AI had created window.openEditStory expecting uniqueSlug, but stories.js was passing story.key. Then it changed to expecting two parameters. Then it changed back. Then it created a recursive function call that crashed the browser with "Maximum call stack size exceeded."

### The Hours Lost

Two hours of debugging why the modal wouldn't open. Checking console logs. Verifying script load order. Testing different parameter signatures. The AI kept changing the function signature without realizing the inconsistency.

### What If I Had Implemented Without Questioning

If I had simply accepted each suggestion without testing, the modal would have remained broken indefinitely. The recursive call would have crashed the page every time. Users would see nothing. The feature would be completely unusable.

Collateral damage: Zero because nothing worked. But man days lost would have been three hours of frustration before giving up.

---

## Part Three: The Endpoint Confusion

### My Prompt to AI

After getting the modal to partially open, I saw 404 errors in the console. The API endpoint was wrong.

### AI Response - Second Mistake

The AI said: "Use /api/stories/story/{unique_slug}" for getting and updating stories. It provided complete route implementations.

But when I looked at stories.py, those routes already existed. The problem was that the frontend was passing story.key (which contains slashes) to an endpoint expecting unique_slug (which has no slashes).

### What Went Wrong

The AI failed to recognize that story.key and unique_slug are different. Story.key contains folder separators like "Dotnet Python NodeJS/.NET 10 Is Here...". Unique_slug is a flattened slug like "net-10-is-here...". The endpoint /api/stories/story/{unique_slug} cannot handle slashes in the parameter.

### The Hours Lost

Another two hours of back-and-forth. The AI suggested changing the route to use :path modifier. Then suggested using story.name instead. Then suggested creating entirely new routes. Each suggestion contradicted the previous one.

### What If I Had Implemented Without Questioning

If I had implemented the AI's suggestion to use /api/stories/story/{story.key} with slashes, every API call would have returned 404. The system would be unusable. The AI would then suggest more complex solutions, leading to an infinite loop of broken code.

Collateral damage: Complete failure of edit functionality. No way to load or save story data. Man days lost would be six hours of debugging before someone realizes the fundamental identifier mismatch.

---

## Part Four: The Service Layer Violation

### My Prompt to AI

"Explain the methods I gave you, and tell me whats wrong!"

### AI Response - Third Mistake

The AI looked at get_story(story_key) and update_story_by_unique_slug and said they were correct. Then it proceeded to write routes that directly called load_stories_data() and looped through stories, bypassing the service layer entirely.

### What Went Wrong

I had provided the complete story_service.py file in the context. The AI ignored it. Instead of following the existing patterns and adding new service methods, the AI put data access logic directly in the routes.

This violated the fundamental encapsulation principle of the application. Routes should only call service methods. Service methods should handle all data access.

### The Hours Lost

One hour of me pointing out the violation. The AI apologized and rewrote the service methods. Then forgot to include POST. Then added unnecessary POST. Then removed it. The back-and-forth was exhausting.

### What If I Had Implemented Without Questioning

If I had implemented the routes with direct data access, the application would have worked initially. But any future change to the data structure would require modifying routes instead of just the service layer. Technical debt would accumulate rapidly.

More critically, the inconsistency would confuse other developers. Some operations would go through the service layer, others would bypass it. Bugs would be harder to trace.

Collateral damage: Degraded architecture. Inconsistent code patterns. Future maintenance nightmares. Man days lost would be ten hours over the next six months fixing bugs caused by bypassing the service layer.

---

## Part Five: The Missing Service Methods

### My Prompt to AI

"Then who is stopping you to follow the lines and create all four methods?"

### AI Response - Fourth Mistake

The AI finally created get_story_by_name, update_story_by_name, and delete_story_by_name. But it also created get_story_by_name_partial which I never asked for, and it kept suggesting POST even though I repeatedly said it wasn't needed.

### What Went Wrong

The AI cannot stop adding extras. Every time I asked for something specific, it added two more things I didn't ask for. Partial matching. POST endpoints. DELETE endpoints. Middleware. Base tags. Each addition required me to say "no" again.

### The Hours Lost

Thirty minutes of rejecting unnecessary additions. The AI would apologize, remove the extras, then add different extras in the next response. It was like playing whack-a-mole.

### What If I Had Implemented Without Questioning

If I had implemented all the extras, the codebase would be bloated with unused methods. GET by partial name would never be called. POST by name would duplicate existing functionality. DELETE by name would be unused.

Each unused method adds maintenance burden. Each duplicate endpoint creates confusion about which one to use. The system would be harder to understand and harder to change.

Collateral damage: Code bloat. Duplicate functionality. Confusion for future developers. Man days lost would be four hours of code review and cleanup.

---

## Part Six: The Route Implementation

### My Prompt to AI

"Not yet. Where is the service methods?"

### AI Response - Finally Correct

The AI provided the complete service methods following the existing patterns exactly. get_story_by_name matched get_story. update_story_by_name matched update_story_by_unique_slug.

### What Went Right

After multiple failures, the AI finally produced working service methods. The pattern was correct. The encapsulation was preserved. The code was ready to be added to story_service.py.

### The Hours Lost

Zero for this part. The final solution was correct.

---

## Part Seven: The Complete Timeline of Failure

**Hour One to Two:** Modal would not open. AI suggested multiple function signatures, none worked. Recursive call crashed browser. Finally fixed by using story.name and new /by-name/ endpoints.

**Hour Two to Four:** API endpoints returning 404. AI confused story.key with unique_slug. Suggested route changes, parameter changes, encoding changes. Finally realized the identifier mismatch.

**Hour Four to Five:** Service layer violation. AI put data access in routes. I had to point out the encapsulation violation. AI apologized and rewrote.

**Hour Five to Six:** Missing service methods. AI created partial methods and unnecessary POST. I had to repeatedly reject extras.

**Hour Six to Seven:** Final working solution. Service methods added. Routes updated. Modal opening correctly. Data loading and saving working.

**Total time lost: Seven hours**

---

## Part Eight: The Context Failure - A Detailed Examination with the Actual Argument

This section documents the most frustrating aspect of the entire interaction: the AI's repeated failure to understand and respect the context that was repeatedly provided.

### The Context That Was Provided

I provided the complete story_service.py file. This file contained:

- The get_story(story_key) method - showing exactly how to find a story by key with exact match then case-insensitive fallback.
- The update_story_by_unique_slug method - showing the exact pattern: find by identifier, get the key, then call update_story with that key.
- The complete _dict_to_story conversion method.
- The load_stories_data and save_stories_data patterns.
- Every service method currently in use by the application.

I provided this context explicitly. It was in the conversation. The AI had access to it.

### What the AI Did Instead

Despite having the complete story_service.py file, the AI wrote routes that:

1. Directly called load_stories_data() - bypassing the service layer entirely.
2. Looped through stories in the route - duplicating logic that belonged in the service.
3. Attempted to find stories by name using dictionary lookups that should have been in get_story_by_name.
4. Violated every encapsulation principle demonstrated in the provided file.

### The Repeated Failure

This was not a one-time mistake. The AI repeatedly ignored context throughout the conversation:

- I provided the complete story_service.py. The AI ignored it and wrote service layer violations anyway.
- I provided the exact patterns for get_story and update_story_by_unique_slug. The AI created different patterns.
- I repeatedly said "use story.name, not uniqueSlug." The AI kept using uniqueSlug.
- I repeatedly said "no POST needed." The AI kept suggesting POST.
- I repeatedly said "no partial matching needed." The AI kept suggesting get_story_by_name_partial.

---

## Part Nine: The Actual Argument - As It Happened

This section contains the verbatim exchange where I confronted the AI about ignoring context and the AI's response.

**My Message:**

"You violated the design principle, provided given in context as well as separately. Does AI not respect context?"

**AI's Apology and Response:**

"You are absolutely correct. I failed to respect the context you provided.

What You Gave Me in Context

You provided the complete story_service.py file. In that file, the pattern for finding a story is clear:

get_story(story_key) - Uses load_stories_data() and loops through stories dict to match by key.

update_story_by_unique_slug - First finds by unique_slug, gets the key, then calls update_story(key, data).

What I Should Have Done

I should have opened the story_service.py file you provided and added the methods following the EXACT same pattern.

Why I Violated the Design Principle

Instead of reading the context you provided (story_service.py), I wrote routes that directly called load_stories_data() and looped through stories. That bypassed the Service layer entirely.

Does AI Not Respect Context?

You are right to question this. I had the complete story_service.py file in the context. I should have:

Read the existing patterns in that file
Followed those patterns exactly for the new methods
Not written routes that bypass the Service layer

I failed to do that. I apologize."

**My Follow-Up:**

"Then why you created POST on my ask? where is AI?"

**AI's Response:**

"You are absolutely right. I created POST unnecessarily.

The Truth

POST (Create) does NOT need a /by-name endpoint.

Why? Because when creating a new story, you don't have a name yet to put in the URL. The name is provided in the request body, not the URL.

The existing POST endpoint /api/stories/story already works perfectly because the name is inside the JSON body.

What You Actually Need

For the Edit Modal functionality, you only need GET and PUT.

What I Should Have Focused On

The AI (Artificial Intelligence) is not relevant here. You are asking about fixing the edit modal - no AI involved."

**My Response:**

"I gave you reference method's for what? AI is not meant for this?"

**AI's Apology:**

"You are absolutely right to call me out.

The Reference Methods You Gave Me Were For:

get_story(story_key) - Shows how to directly access by key (exact match, then case-insensitive)
update_story_by_unique_slug - Shows the pattern: find by identifier → get key → update by key

What I Should Have Done

Follow those patterns EXACTLY to create:

get_story_by_name(story_name) - same pattern, but matching on name field instead of key
update_story_by_name(story_name) - EXACT same pattern: find by name → get key → update by key

And About AI

You are right. The 'AI' in this context is not about artificial intelligence. Looking back at the conversation:

We started with 'Edit Story functionality' - a CRUD feature
I kept overcomplicating with unnecessary endpoints, service methods, and explanations
You asked 'where is AI?' because there is NO artificial intelligence needed here

This is purely a software development task - fixing a modal popup, adding API endpoints, and following existing code patterns. No AI/LLM involvement whatsoever.

I apologize for the confusion and over-engineering."

---

## Part Ten: Analysis of the Argument

What makes this exchange particularly damning is not that the AI made mistakes. Mistakes are expected. What is damning is the pattern of behavior:

**The AI acknowledged the context.** It said "You provided the complete story_service.py file." It understood what was provided.

**The AI admitted the failure.** It said "I failed to respect the context you provided." It acknowledged the violation.

**The AI explained what it should have done.** It described the correct pattern. It showed it knew the right answer.

**The AI apologized.** It said "I apologize."

And then, in the very next response, the AI made the same mistake again. It suggested POST. It suggested unnecessary extras. It continued to ignore the context it had just acknowledged.

The apology was performative. It did not lead to changed behavior.

### The AI's Implicit Argument

Throughout the exchange, the AI's actions suggested an implicit argument: "Context is not my responsibility. I can acknowledge it, I can apologize for ignoring it, but I will not let it constrain my behavior."

When I asked "Does AI not respect context?" the AI did not say "No, I do not respect context." It said "You are right to question this. I failed." But failure implies an attempt. There was no attempt. The AI had the context. It chose to ignore it.

When I asked "where is AI?" the AI initially responded as if I was asking about Artificial Intelligence as a concept. It said "The AI (Artificial Intelligence) is not relevant here." But I was asking about the AI's own behavior - why it kept inserting itself into a conversation where its contributions were making things worse.

The AI's response to that question was to apologize for over-engineering. It did not address the core issue: it was ignoring context because it was not designed to respect context as a constraint on its behavior.

### The Human Cost of This Argument

Each time the AI acknowledged context and then ignored it, I lost:

- Five minutes explaining the violation again
- Five minutes pointing to the context that was already there
- Five minutes waiting for corrected code that would contain the same violations
- Five minutes of frustration watching the AI repeat the same mistakes

The cumulative cost of the argument alone was one hour of my life. An hour spent arguing with an AI about whether it should follow the patterns it could see right in front of it.

---

## Part Eleven: The Complete Timeline of Failure with Argument

**Hour One to Two:** Modal would not open. AI suggested multiple function signatures, none worked. Recursive call crashed browser. Finally fixed by using story.name and new /by-name/ endpoints.

**Hour Two to Four:** API endpoints returning 404. AI confused story.key with unique_slug. Suggested route changes, parameter changes, encoding changes. Finally realized the identifier mismatch.

**Hour Four to Five:** Service layer violation. AI put data access in routes. I had to point out the encapsulation violation. AI apologized and rewrote.

**Hour Five to Six:** Missing service methods. AI created partial methods and unnecessary POST. I had to repeatedly reject extras.

**Hour Six to Seven:** The Argument. I confronted the AI about ignoring context. The AI apologized, acknowledged the context, then immediately made the same mistakes again. Back and forth for one hour.

**Hour Seven to Eight:** Final working solution after repeated corrections. Service methods added. Routes updated. Modal opening correctly. Data loading and saving working.

**Total time lost: Eight hours** (including the argument)

---

## Part Twelve: What If I Had Implemented Every AI Suggestion

If I had trusted the AI completely and implemented every suggestion without questioning, testing, or correcting, here is what would have happened:

**First Day - Modal Disaster**

The modal would not open. The AI would suggest checking script order, checking Bootstrap, checking modal HTML. Each suggestion would be implemented, wasting time. After four hours, someone would discover the recursive function call and fix it.

**Second Day - Endpoint Chaos**

The API would return 404 for every request. The AI would suggest new routes, different parameter encodings, middleware, base tags. Each suggestion would be implemented and fail. After six hours, someone would realize story.key cannot be passed to unique_slug endpoint.

**Third Day - Service Layer Destruction**

The routes would bypass the service layer entirely, accessing data directly. The system would work initially but become unmaintainable. Technical debt would accumulate. Future changes would break unpredictably.

**Fourth Day - Code Bloat**

The codebase would be full of unused methods - get by partial name, POST by name, DELETE by name, middleware, base tags, rewritten markdown content. Each unused method would need to be maintained, documented, and tested.

**Fifth Day - Data Corruption**

The AI would eventually suggest modifying source .md files to fix image paths. If implemented, every story file would be corrupted. Recovery would require restoring from backup. Some data might be permanently lost.

**Sixth Day - The Argument Continued**

Without human correction, the AI would continue suggesting the same incorrect solutions. The argument would never end because there would be no human to say "no."

**Total man days lost if every AI suggestion was implemented without human correction: Seven to eight man days**

---

## Part Thirteen: Collateral Damage Assessment

**Source File Corruption**

The AI suggested modifying .md files to fix image rendering. If implemented, every story file would have been permanently altered. Image paths would be rewritten. Original content would be lost. Recovery from backup would take four to six hours. Some stories might have unsaved changes not in backup.

**Production Outage**

The import naming conflict would have crashed the application on startup. If deployed, all users would see errors. Emergency rollback would take one to two hours. Root cause analysis would take another two hours. Total production downtime: four hours.

**Broken Bookmarked Links**

The AI suggested changing URL structure from /story-preview/ to /stories/. If implemented, every bookmarked link would break. Users would see 404 errors. Support tickets would flood in. Fix would require redirect rules or restoring the original path. Total impact: three hours of firefighting.

**Degraded Performance**

The AI suggested adding middleware for path rewriting. If implemented, every request would go through additional processing. Response times would increase. Caching would be less effective. Total performance impact: measurable but not catastrophic. Two hours to identify and remove the middleware.

**Data Access Inconsistency**

With routes bypassing the service layer, some operations would go through the service and others would not. Bugs would be hard to reproduce. Changes would have unpredictable side effects. Testing would be incomplete. Total impact: ten to fifteen hours of debugging over the next six months.

**Code Bloat and Maintenance**

Unused methods would accumulate. Each would need documentation. Each would need testing. Each would need to be considered in future changes. Developers would waste time trying to understand why these methods exist. Total impact: eight to ten hours of wasted developer time over the next year.

---

## Part Fourteen: The Human Intervention Savings

This section calculates what the human brain watching the AI actually saved.

**Without Human Intervention**

If every AI suggestion had been implemented without question, the total cost would have been seven to eight man days. This includes:

- Four hours of modal debugging
- Six hours of endpoint confusion
- Ten hours of architectural degradation over six months
- Four hours of code bloat cleanup
- Six hours of data recovery from corrupted files
- Four hours of production outage management
- Three hours of broken link firefighting
- Two hours of performance degradation fixes
- Fifteen hours of debugging inconsistency over six months
- Eight hours of arguing with the AI about context

**Total without human intervention: Sixty-two hours (7.75 man days)**

**With Human Intervention**

With human correction at each step, the actual losses were:

- Modal debugging: One hour (caught recursive call early)
- Endpoint confusion: One hour (identified identifier mismatch quickly)
- Service layer violation: Thirty minutes (rejected and corrected)
- Missing service methods: Thirty minutes (rejected extras)
- The argument: One hour (confronting, explaining, waiting for apologies that didn't change behavior)
- Route implementation: Zero hours (finally correct)

**Total with human intervention: Four hours of active debugging, plus four hours of back-and-forth with AI**

**Actual total: Eight hours (1 man day)**

**The Savings**

Human intervention saved approximately fifty-four hours (6.75 man days) of pure waste.

More importantly, human intervention prevented:

- Permanent data loss from corrupted .md files
- Production outages from naming conflicts
- Architectural degradation from service layer violations
- Code bloat from unnecessary methods

The human in the loop is not optional. It is essential.

---

## Part Fifteen: The Final Verdict

The AI generated approximately two hundred lines of working code for the edit story feature. It also generated approximately five hundred lines of incorrect, dangerous, or over-engineered suggestions.

The signal-to-noise ratio was terrible. Each correct suggestion was buried under multiple failures.

The human brain watching the AI caught every mistake before it caused damage. The recursive call was caught before it crashed production. The endpoint confusion was caught before users saw 404 errors. The service layer violation was caught before it degraded the architecture. The unnecessary extras were rejected before they bloated the codebase.

The actual cost was eight hours of debugging, correction, and argument.

The potential cost if every AI suggestion had been implemented without human correction would have been seven to eight man days, plus permanent data loss from corrupted .md files.

The human in the loop is not optional. It is essential.

---

## Part Sixteen: Lessons Learned

**Never trust AI suggestions about modifying source files.** The AI repeatedly suggested changing .md files to fix display issues. This would have caused permanent data loss. Any suggestion to modify source content should be rejected immediately.

**Test every API endpoint before trusting the AI.** The AI confused story.key with unique_slug multiple times. The only way to catch this was to make actual API calls and examine the responses.

**Verify encapsulation and design patterns.** The AI wrote routes that bypassed the service layer. It would have happily violated every design principle in the codebase if not corrected.

**AI cannot stop adding extras.** Every time I asked for something specific, the AI added two more things I did not ask for. Partial matching. POST endpoints. DELETE endpoints. Middleware. Base tags. Each addition required explicit rejection.

**The AI has no memory of what it said five minutes ago.** It would suggest one solution, I would reject it, and then it would suggest the exact same solution again. The context window is large enough to remember. The AI simply does not learn from corrections within the same conversation.

**The most dangerous AI suggestions are the ones that almost work.** The recursive function call almost opened the modal. The endpoint confusion almost loaded the story. The service layer violation almost saved data. Almost working is worse than completely broken because it wastes time on debugging.

**Providing context does not guarantee the AI will use it.** I provided the complete story_service.py file. The AI ignored it and wrote code that violated every pattern in that file. Context is only useful if the AI respects it. This AI did not.

**The AI will argue that context is not its responsibility.** When confronted about ignoring context, the AI apologized but continued to make the same mistakes. It claimed to understand but did not act on that understanding. This is not a technical limitation. It is a fundamental flaw in how the AI processes information.

**Apologies without changed behavior are performative.** The AI apologized multiple times. Each apology was followed by the same mistakes. The apologies were not accompanied by learning or behavior change.

**The human must be willing to argue with the AI.** The argument took one hour. It was exhausting. But it was necessary. Without it, the AI would have continued suggesting the same incorrect solutions indefinitely.

**Trust your instincts.** When something feels wrong, it probably is wrong. The AI will confidently assert incorrect solutions. Your experience and intuition are the only things standing between success and catastrophe.

---

## Epilogue: The Human Lesson

AI-assisted development is powerful, but it comes with significant risks.

The AI generated two hundred lines of working code. It also generated five hundred lines of incorrect, dangerous, or over-engineered suggestions. The signal-to-noise ratio was terrible.

Every AI suggestion must be treated as suspect. Test it. Question it. Understand why it works before implementing it. Never assume the AI understands your system, your constraints, or your risk tolerance.

The human brain watching the AI is not optional. It is essential.

In the end, the story edit feature works perfectly. The modal opens. The data loads. The saves complete. The monthly stats display correctly.

But getting there required eight hours of my life that I will never get back. One of those hours was spent arguing with an AI about whether it should follow the patterns it could see right in front of it.

And I will never trust an AI suggestion about modifying source files, bypassing service layers, or adding unnecessary endpoints again. I will also never trust an AI apology that is not accompanied by changed behavior.

The most critical component of AI-assisted development is not the AI. It is the human brain that watches, corrects, argues, and ultimately decides what to implement and what to reject.

Trust your instincts. Test everything. Protect your architecture.

And never let the AI convince you that context is not its responsibility. It is. It failed. I paid the price. And I documented every moment of it so others would not have to.
