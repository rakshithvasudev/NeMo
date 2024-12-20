# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nemo.collections.common.prompts.formatter import BOS_SLOT, EOS_SLOT, Modality, PromptFormatter


class Llama2PromptFormatter(PromptFormatter):
    """
    This template has been validated to provide identical tokenized results to the official code
    in https://github.com/meta-llama/llama/blob/main/llama/generation.py
    """

    NAME = "llama2"
    OUTPUT_ROLE = "assistant"
    TEMPLATE = {
        "system_and_user": {
            "template": f"{BOS_SLOT}[INST] <<SYS>>\n|system|\n<</SYS>>\n\n|message| [/INST]",
            "slots": {
                "system": Modality.Text,
                "message": Modality.Text,
            },
        },
        "user": {
            "template": "|bos|[INST] |message| [/INST]",
            "slots": {
                "message": Modality.Text,
            },
        },
        OUTPUT_ROLE: {
            "template": f"|message| {EOS_SLOT}",
            "slots": {
                "message": Modality.Text,
            },
        },
    }


LLAMA3_BOS = "<|begin_of_text|>"
LLAMA3_HEADER_BEGIN = "<|start_header_id|>"
LLAMA3_HEADER_END = "<|end_header_id|>"
LLAMA3_END_OF_TURN = "<|eot_id|>"
LLAMA3_NL = "\n\n"


class Llama3PromptFormatter(PromptFormatter):
    """
    Implemented following the code at:
     https://github.com/meta-llama/llama3/blob/main/llama/test_tokenizer.py#L56
    """

    NAME = "llama3"
    OUTPUT_ROLE = "assistant"
    TEMPLATE = {
        "preamble": {
            "template": LLAMA3_BOS,
        },
        "system": {
            "template": f"{LLAMA3_HEADER_BEGIN}system{LLAMA3_HEADER_END}{LLAMA3_NL}|message|{LLAMA3_END_OF_TURN}",
            "slots": {
                "message": Modality.Text,
            },
        },
        "user": {
            "template": f"{LLAMA3_HEADER_BEGIN}user{LLAMA3_HEADER_END}{LLAMA3_NL}|message|{LLAMA3_END_OF_TURN}",
            "slots": {
                "message": Modality.Text,
            },
        },
        OUTPUT_ROLE: {
            "template": f"{LLAMA3_HEADER_BEGIN}assistant{LLAMA3_HEADER_END}{LLAMA3_NL}|message|{LLAMA3_END_OF_TURN}",
            "slots": {
                "message": Modality.Text,
            },
        },
    }
