# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
# ---

# %%
# https://github.com/matplotlib/matplotlib/issues/5836#issuecomment-179592427
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import matplotlib.pyplot as plt

# %% [markdown]
# # Tikzの動作確認
#
# このノートはTikzの動作確認を行うために作成したものです。

# %%
# ```{tikz}
# :include: example.tikz
# ```