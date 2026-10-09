"""Reject malformed or accidental private fields before public deployment."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

FIELDS = {'id','industry','title_en','title_zh','price','revenue','ebitda','angle_en','angle_zh','checked_at'}

def timestamp(value):
    assert isinstance(value, str), 'Timestamp must be a string'
    dt = datetime.fromisoformat(value.replace('Z','+00:00'))
    assert dt.tzinfo is not None, 'Timestamp must include timezone'
    assert dt <= datetime.now(timezone.utc), 'Timestamp is in the future'
    return dt

def validate(data):
    assert set(data) == {'schema_version','updated_at','deals'}, 'Unknown top-level fields'
    assert type(data['schema_version']) is int and data['schema_version'] == 1
    assert isinstance(data['deals'], list) and len(data['deals']) <= 6
    if data['updated_at'] is None:
        assert not data['deals'], 'Unpublished feed must be empty'
    else:
        updated = timestamp(data['updated_at'])
    seen = set()
    for deal in data['deals']:
        assert isinstance(deal, dict) and set(deal) == FIELDS, 'Unknown/missing deal fields'
        for key, value in deal.items():
            assert isinstance(value,str) and 0 < len(value) <= 600, f'Invalid {key}'
            assert '<' not in value and '>' not in value, 'HTML is not accepted'
            assert 'http://' not in value.lower() and 'https://' not in value.lower(), 'Keep source URLs private'
            assert '@' not in value, 'Keep contact emails private'
        assert deal['id'] not in seen, 'Duplicate deal reference'
        seen.add(deal['id'])
        assert timestamp(deal['checked_at']) <= updated, 'Checked time exceeds snapshot time'
    return True

if __name__ == '__main__':
    try:
        validate(json.loads(Path(sys.argv[1]).read_text()))
    except (AssertionError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f'Feed validation failed: {exc}')
    print('Public feed is valid.')
