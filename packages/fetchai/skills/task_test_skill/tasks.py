# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 Valory AG
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module contains the tasks for the 'task test skill' skill."""
import time
from typing import Any

from aea.skills.tasks import Task


class SimpleTask(Task):
    """Simple task."""

    def __init__(self, data: Any):
        """Initialize the task."""
        super().__init__()
        self.data = data

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """Execute task."""
        time.sleep(3)
        return self.data
