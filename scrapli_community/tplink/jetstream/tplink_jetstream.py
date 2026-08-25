"""scrapli_community.tplink.jetstream.tplink_jetstream"""

from scrapli.driver.network.base_driver import PrivilegeLevel
from scrapli_community.tplink.jetstream.async_driver import default_async_on_close, default_async_on_open
from scrapli_community.tplink.jetstream.sync_driver import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "exec": (
        PrivilegeLevel(
            pattern=r"^[\*\s]*(.*)\>\s*$",
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
            pattern=r"^[\*\s]*(.*)\#\s*$",
            name="privilege_exec",
            previous_priv="exec",
            escalate="enable",
            deescalate="exit",
            escalate_auth=True,
            escalate_prompt=r"^\s*[pP]assword:\s*$",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[\*\s]*(.*)\#\s*$",
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
        "auth_telnet_login_pattern": r"^\s*[Uu]ser:\s*$",
        "auth_password_pattern": r"^\s*[Pp]assword:\s*$",
        "comms_return_char": "\r",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "Error:",
        ],
        "textfsm_platform": "",
        "genie_platform": "",
    },
}
