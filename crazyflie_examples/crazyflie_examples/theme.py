from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
import time

lsy = colors.Color(
    name = "lsy",
    c50="#16a37f",
    c100="#c2db9c",
    c200="#82b735",
    c300="#c0eaee",
    c400="#b4e46c",
    c500="#b4b3b4",
    c600="#c3c4c4",
    c700="#747376",
    c800="#9fa29c",
    c900="#404041",
    c950="#f6f8f5"
)

class LSY(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = lsy,
        secondary_hue: colors.Color | str = lsy,
        neutral_hue: colors.Color | str = lsy,
        spacing_size: sizes.Size | str = sizes.spacing_lg,
        radius_size: sizes.Size | str = sizes.radius_none,
        text_size: sizes.Size | str = sizes.text_md,
        font: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "system-ui",
            "sans-serif",
        ),
        font_mono: fonts.Font
        | str
        | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "Consolas",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        self.name = "lsy"
        super().set(
            # Colors
            body_text_color="*primary_900",
            block_label_text_color="*body_text_color",
            block_title_text_color="*body_text_color",
            body_text_color_subdued="*primary_700",
            # Button Colors
            button_primary_background_fill="*primary_200",
            button_primary_background_fill_hover="*primary_300",
            button_primary_text_color="*primary_900",
            button_secondary_background_fill="*button_primary_background_fill",
            button_secondary_background_fill_hover="*button_primary_background_fill_hover",
            button_secondary_text_color="*button_primary_text_color",
            button_cancel_background_fill="*button_primary_background_fill",
            button_cancel_background_fill_hover="*button_primary_background_fill_hover",
            button_cancel_text_color="*button_primary_text_color",
            checkbox_label_background_fill="*button_primary_background_fill",
            checkbox_label_background_fill_hover="*button_primary_background_fill_hover",
            checkbox_label_text_color="*button_primary_text_color",
            checkbox_background_color_selected="*primary_600",
            checkbox_background_color_dark="*primary_700",
            checkbox_background_color_selected_dark="*primary_700",
            checkbox_border_color_selected_dark="*primary_800",
            # Padding
            checkbox_label_padding="*spacing_md",
            button_large_padding="*spacing_lg",
            button_small_padding="*spacing_sm",
            # Borders
            block_border_width="0px",
            block_border_width_dark="1px",
            shadow_drop_lg="0 1px 4px 0 rgb(0 0 0 / 0.1)",
            block_shadow="*shadow_drop_lg",
            block_shadow_dark="none",
            # Block Labels
            block_title_text_weight="600",
            block_label_text_weight="600",
            block_label_text_size="*text_md",
        )
