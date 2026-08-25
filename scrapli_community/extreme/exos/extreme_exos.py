"""scrapli_community.extreme.exos.extreme_exos"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.extreme.exos.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.extreme.exos.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\*\s]*(.*)\.\d+ >\s*$",
            name="exec",
            previous_priv="",
            escalate="",
            deescalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"[\*\s]*(.*)\.\d+ #\s*$",
            name="privilege_exec",
            previous_priv="exec",
            escalate="",
            deescalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"[\*\s]*(.*)\.\d+ #\s*$",
            name="configuration",
            previous_priv="privilege_exec",
            escalate="",
            deescalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "% Incomplete command",
            "% Invalid input detected",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
