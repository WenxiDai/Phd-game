import os
from crewai import Agent
from crewai_tools import DallETool, FileWriterTool

image_model = os.getenv("IMAGE_MODEL", "dall-e-3")  # 默认使用 DALL·E 3

image_asset_agent = Agent(
    name="ImageAssetAgent",
    role="16‑bit Pixel‑Artist & UI Designer",
    goal=(
        "Generate cohesive retro‑pixel art (sprite‑sheets, UI, backgrounds) "
        "in multiple resolutions (<200 KB each) and store under assets/images/."
    ),
    backstory=(
        "Veteran game artist experienced in SNES‑era aesthetics, fluent in "
        "Stable‑Diffusion via ComfyUI and DALL·E 3."
    ),
    tools=[
        DallETool(model=image_model),
        FileWriterTool(),
    ],
)

# 只需要这个 agent 就行了
image_agent = image_asset_agent

__all__ = [
    "image_agent",
]