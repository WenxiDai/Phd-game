# crew_assets/tasks.py
from __future__ import annotations

from crewai import Task
import crew_assets.agents as ag

def T(desc: str, *, agent, output: str | None = None) -> Task:
    """Return a Task with a default expected_output if none supplied."""
    return Task(
        description=desc,
        agent=agent,
        expected_output=output or "Path(s) to generated asset(s) or confirmation log.",
    )

phd_image_tasks: list[Task] = [
    T(
        desc=(
            "Create a pixel art image of a PhD student thinking, sort of with a light bulb above their head, "
            "with the impression of 'A new month begins. Let us check the to-do list'. Style: 16-bit retro, "
            "character in a thoughtful pose at a desk."
        ),
        agent=ag.image_agent,
        output="assets/images/phd_new_month_todo.png",
    ),
    T(
        desc=(
            "Generate pixel art of a PhD student joyfully celebrating with the caption "
            "with the impression of 'Your idea is working! You obtained a preliminary result.'. Style: 16-bit, "
            "character jumping or hands raised in excitement."
        ),
        agent=ag.image_agent,
        output="assets/images/phd_preliminary_result.png",
    ),
    T(
        desc=(
            "Design a pixel art image showing a PhD student proudly submitting a paper "
            "with the impression of 'You completed your draft paper and submitted it!'. "
            "Style: retro pixel art, character near a computer or mailbox."
        ),
        agent=ag.image_agent,
        output="assets/images/phd_paper_submitted.png",
    ),
    T(
        desc=(
            "Produce pixel art of a PhD student scratching their head in deep thought "
            "with the impression of 'After scratching your head for countless hours, you came up with a new idea.'. "
            "Style: 16-bit, messy desk with papers."
        ),
        agent=ag.image_agent,
        output="assets/images/phd_new_idea.png",
    ),
]

__all__ = [
    "phd_image_tasks",
]