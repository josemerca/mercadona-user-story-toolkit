Author: Various authors
Source: Various sources

# Heuristics for User Story Documentation and Splitting

This document extracts heuristics from the provided sources regarding user story documentation and splitting, aimed at maximizing impact and minimizing effort within iterative delivery.

## The Process and Principles

User stories are fundamentally about **collaboration, not hand-overs**. They represent a model where requirements **emerge through frequent involvement and discussions** between business stakeholders and delivery teams.

*   Instead of writing down detailed requirements upfront, **tell stories**. Physical or electronic tools serve primarily as **reminders for conversations**.
*   These discussions are critical for the delivery team to correctly understand what business stakeholders want, discovering functional gaps and unclear requirements faster, and leading to **better solutions** by leveraging shared knowledge.
*   Approach stories as **survivable experiments** to test assumptions about business value. The **size of a story should reflect how much business stakeholders are willing to invest in learning** if a proposed change delivers the assumed value, rather than simply fitting into an iteration. This shifts focus from technical complexity to expected outcomes and learning.
*   Manage the big picture using **hierarchical backlogs**, such as **Impact Maps** or **User Story Maps**. This avoids being overwhelmed by a flat list of too many small stories ("story card hell") and allows planning and prioritization at higher levels.
*   Organize backlogs by **grouping stories by impact**. **Impact maps** specifically link deliverables (stories) to impacts (behaviour changes) and business goals, making the connection visible and helping prioritize based on desired outcomes.
*   **Name your milestones** meaningfully, reflecting the increment of business value or capability each milestone intends to deliver (e.g., 'Mobile users can buy concert tickets', 'PCI compliance satisfied').
*   To achieve focus and reduce scope, **focus milestones on a limited number of user segments**. Select target segments first, then prioritize stories based on those choices.
*   During story discussions, **imagine the demonstration** of the completed story. This helps clarify acceptance criteria, focuses the team on the outcome, and encourages splitting larger stories to deliver a demonstrable piece sooner.
*   Consider **splitting business and technical discussions** into separate sessions to use business stakeholders' time efficiently and allow technical teams to discuss design implications.
*   Understand the value chain by **investigating value on multiple levels** (e.g., user value vs. organizational value). Making this clear aids discussion and validation of assumptions.
*   **Don't push everything into stories**. Technical tasks, internal improvements, or infrastructure work that do not deliver direct end-user value should be managed separately, perhaps with a dedicated time budget.
*   **Throw stories away after they are delivered**. Stories are **conversation tokens**, not documentation of the final system. Manage completed specifications and tests by functional area instead, to describe the current system accurately.
*   Use **low-tech tools** like whiteboards and sticky notes for initial story conversations to facilitate flexibility and collaboration, digitizing only after the discussion is complete.
*   Employ techniques like **Diverge and Merge** to structure discussions and ensure participation.
*   Involve all roles in the discussion.
*   Use **feedback exercises** to measure alignment and objectivity in discussions.
*   Play the **devil's advocate** to intentionally challenge assumptions and identify potential problems early.
*   **Divide responsibility for defining stories**: business stakeholders specify the 'As a...' and 'In order to...' (the problem/value), and the delivery group proposes 'I want...' (the solution).
*   Define **global concerns or cross-cutting concerns** (like security, performance, usability) at the start of a milestone, rather than per story. Techniques include FURPS+ or a Quality Pyramid.
*   Use the **Purpose Alignment model** to categorize work and identify if parity/partner items should be built internally or integrated/outsourced.
*   Create a **Stakeholder Chart** to understand different groups' interest and power and how to engage with them.
*   **Check outcomes with real users** after delivering stories to see if intended behaviour changes or impacts materialized.
*   Consider **staged releases** or opt-in for large user interface changes to reduce risk and get feedback.
*   **Split UX improvement research** (learning) from ongoing implementation (earning).

## Documentation Heuristics

While stories aren't full documentation, key information should be captured to guide discussions and development:

*   **Describe a behaviour change:** Focus on the **observable and measurable change** in behaviour expected as a result of the story. Quantify it where possible. Use phrases like "**Whereas currently...**" or "**Instead of...**" to highlight the difference from current behaviour.
*   **Describe the system change:** Complement the behaviour change by describing the system-level modifications involved. Clarify how it differs from the current system.
*   **Avoid generic roles:** **Do not use "As a user..." or other overly generic roles**. Identify and describe the **specific user segment or persona** who will benefit.
*   **Evaluate zone of control and sphere of influence:** Understand if the desired outcome is within the delivery team's control or relies on external factors.
*   **Put a 'best before' date on stories:** Explicitly note time constraints for time-sensitive work.

## Story Splitting Heuristics

Splitting large stories into smaller, valuable pieces is essential for iterative delivery, enabling faster feedback and value delivery:

*   **Start with the outputs:** Instead of splitting work based on technical inputs or workflows, focus on **delivering specific outputs incrementally**. This makes it easier to create a sensible incremental plan and quickly deliver valuable data.
*   **Forget the walking skeleton – put it on crutches:** Deliver minimal user-facing functionality, potentially using simpler back-end components or manual steps initially, to get something usable into production quickly. Build up the full architecture iteratively later.
*   **Narrow down the customer segment:** Deliver the full required functionality for a **smaller, specific group of users first**, rather than partial functionality for everyone. This is useful when perceived basic functionality is large.
*   **Split by examples of usefulness:** For large technical changes, list concrete examples of how the change will be useful. Identify examples that can be delivered with only a **subset of the full technical solution** and turn these into separate stories.
*   **Split by capacity:** Create smaller stories by limiting the scope based on system capacity, such as file size, number of users, or data volume. Deliver for a lower capacity first.
*   **Start with dummy, then move to dynamic:** For features requiring complex data integration, first build the interface and workflow using simple, **hard-coded (dummy) data**. Follow up with stories to integrate with the real (dynamic) data source. This reduces initial work and speeds up delivery of value.
*   **Simplify outputs:** Reduce the complexity of initial output formats (e.g., use a simple file instead of direct database integration, or one format instead of many). Ensure the simplified output still provides value. This can de-risk short-term plans, especially with legacy or external systems.
*   **Split learning from earning:** Separate research or investigation tasks into time-boxed **learning stories** with the goal of informing planning decisions. **Earning stories** focus purely on delivering value to end-users.
*   **Extract basic utility:** For critical tasks, deliver the **bare minimum functionality** required for a user to complete the task, even if it sacrifices usability or requires manual steps. Prioritize basic utility first, then refine usability later. This is useful for meeting tight deadlines. **Communicate this trade-off clearly**.
*   **Slice the hamburger:** A technique to break down a large piece of work by listing technical components/workflow steps (layers) and quality attributes (options). **Brainstorm options at different quality levels** for each step and choose a 'slice' across layers that delivers value, potentially skipping or simplifying steps.

## Instructions for Maximizing Impact and Minimizing Effort

Drawing from the principles and heuristics:

*   **Prioritize at a higher level:** Instead of prioritizing individual stories, **pick the most important impacts** or focus on key customer segments first. This aligns work with business goals, reduces unnecessary scope, and ensures alignment among stakeholders. Use hierarchical backlogs like Impact Maps to facilitate this.
*   **Focus on value-driven slicing:** Use splitting techniques that break down work based on **delivering value quickly** rather than technical architecture alone. Techniques like 'Start with Outputs', 'Narrow Customer Segment', 'Extract Basic Utility', and 'Split by Examples of Usefulness' are key here.
*   **Reduce scope intentionally:** Techniques like focusing on **limited user segments** and **simplifying outputs** or inputs (dummy data) are explicit strategies for reducing the scope of early deliveries to minimize effort for a given impact or to get *some* value sooner.
*   **Manage risk with small experiments:** Viewing stories as **survivable experiments** helps manage the risk of building the wrong thing by testing assumptions cheaply and quickly. Smaller, valuable stories allow for faster feedback and adaptation.
*   **Ensure collaborative discussion:** Frequent and effective discussions involving both business stakeholders and delivery teams are essential for understanding needs, refining scope, and identifying the most impactful ways to split work. Techniques like **Diverge and Merge**, involving all roles, and playing the devil's advocate improve discussion quality. Dividing story definition responsibility encourages discussion.
*   **Budget for non-story work:** Allocate dedicated time or a budget for necessary technical tasks, maintenance, or foundational work that isn't customer-facing. This prevents it from competing directly with impact-driven stories in prioritization and ensures this necessary work gets done.
*   **Avoid misleading metrics:** Do not rely solely on numeric story sizes for long-term planning or capacity management. They are better used for identifying stories too large for an iteration. Consider estimating capacity based on analysis time or a rolling number of similarly-sized stories.
*   **Continuously check outcomes:** After delivering stories aimed at a behaviour change or impact, **check with real users** to see if the intended outcome materialized. This feedback loop ensures the team is focused on delivering *actual* impact and allows for discarding or revising features that didn't achieve the goal.
*   **Separate learning from earning:** Use time-boxed **learning stories** for research and investigation needed to reduce uncertainty and make informed planning decisions before investing significant effort in delivering features. This minimizes wasted effort on building features based on incorrect assumptions.
*   **Challenge non-differentiating work:** Use the Purpose Alignment model to question whether tasks falling into 'parity' or 'partner' categories should be built internally or could be addressed more efficiently through integration or outsourcing.

## Linguistic Heuristics for Splitting User Stories

Certain words and phrases in user stories can signal that a story is doing too much and could be split into smaller, more focused stories. Watch for these categories:

### 1. Coordinating Conjunctions (and, or, but, yet, nor...)
- **Usage:** If a story says "The user can do X and Y," it's likely two stories: one for X, one for Y.
- **Example:**
  - "As a user, I can upload and download files."
    → Split into "upload" and "download" stories.

### 2. Action-Related Connectors (manage, handle, support, process, maintain, administer...)
- **Usage:** These often hide multiple actions under a generic verb. "Manage" could mean create, update, delete, etc.
- **Example:**
  - "As an admin, I can manage users."
    → Split into "create users," "edit users," "delete users," etc.

### 3. Sequence Connectors (before, after, then, while, during, when...)
- **Usage:** Indicates a process with multiple steps or phases, each of which could be a separate story.
- **Example:**
  - "As a user, I can save my work before submitting."
    → Split into "save work" and "submit work."

### 4. Scope Indicators (including, as-well-as, along with, also, additionally, plus, with...)
- **Usage:** These words often introduce extra requirements or features that can be separated.
- **Example:**
  - "As a user, I can receive notifications via email and SMS."
    → Split into "email notifications" and "SMS notifications."

### 5. Option Indicators (either/or, whether, alternatively, optionally...)
- **Usage:** Options or alternatives usually mean there are multiple paths or features, each of which can be a story.
- **Example:**
  - "As a user, I can log in with a password or with Google."
    → Split into "password login" and "Google login."

### 6. Exception Indicators (except, unless, however, although, despite...)
- **Usage:** Exceptions often point to edge cases or special rules that can be handled separately.
- **Example:**
  - "As a user, I can delete my account unless I am an admin."
    → Split into "user account deletion" and "admin account restrictions."

**Summary:**
Whenever you see these words in a user story, it's a red flag that the story might be too big or trying to do too much. Each connector or indicator is an opportunity to ask, "Can this be split into smaller, more focused stories?" This leads to smaller, clearer, and more testable increments—perfect for lean, incremental delivery.
