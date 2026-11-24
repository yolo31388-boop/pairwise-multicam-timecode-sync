import pytest
import media.multicam_timecode_sync as mod

CASES = [
    ("clock_drift_fix", (1,)),
    ("align_direct_sound", (1,)),
    ("cut_at_keyframe", (1,)),
    ("timecode_wrap", (1,)),
    ("surface_return", (1,)),
    ("post_switch_check", (1,)),
    ("load", (1,)),
    ("align", (1,)),
    ("cut", (1,)),
    ("preview", (1,)),
    ("validate_sync", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
