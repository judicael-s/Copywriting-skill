from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md',
    'SKILL.md',
    'references/drayton-eddie-principles.md',
    'references/micro-lesson-workflow.md',
    'references/hook-discipline.md',
    'references/shared-mental-images.md',
    'references/close-the-loop-endings.md',
    'references/concision-pass.md',
    'references/copy-critique-before-rewrite.md',
    'references/career-application-copywriting.md',
    'references/proof-provenance.md',
    'references/seo-growth-copy-integration.md',
    'references/human-voice-rules.md',
    'skills/career-copywriting/SKILL.md',
    'skills/seo-copywriting/SKILL.md',
    'skills/french-copywriting/SKILL.md',
    'skills/social-copywriting/SKILL.md',
    'skills/tone-of-voice/SKILL.md',
    'examples/landing-page-before-after.md',
    'examples/french-landing-page-example.md',
    'examples/linkedin-micro-lesson-example.md',
    'examples/seo-brief-example.md',
    'examples/tone-of-voice-guide-example.md',
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def test_required_files_exist():
    for rel in REQUIRED_FILES:
        assert (ROOT / rel).exists(), rel


def test_readme_has_no_em_or_en_dashes():
    text = read('README.md')
    assert '—' not in text
    assert '–' not in text


def test_readme_positions_agent_compatibility_and_eddie_style():
    text = read('README.md')
    for required in [
        'Hermes',
        'Open Claw Agent',
        'Claude Code',
        'Codex',
        'More specific.',
        'drayton-eddie-principles.md',
        'career-copywriting',
    ]:
        assert required in text


def test_drayton_eddie_quality_layer_present():
    text = read('references/drayton-eddie-principles.md')
    for required in [
        'one real prospect',
        'complete selling job',
        'Micro-lesson structure',
        'Proof early',
        'Qualify big promises',
    ]:
        assert required in text


def test_hook_and_story_workflows_present():
    for rel, terms in {
        'references/hook-discipline.md': ['Change the entry point', 'entry point by situation'],
        'references/shared-mental-images.md': ['A familiar object can carry meaning', 'Return to the image'],
        'references/close-the-loop-endings.md': ['final line should make the opening feel inevitable'],
        'references/micro-lesson-workflow.md': ['small scene or observation', 'lesson'],
    }.items():
        text = read(rel)
        for term in terms:
            assert term in text


def test_concision_and_proof_rules_present():
    assert 'Cut until the sentence becomes weaker' in read('references/concision-pass.md')
    proof = read('references/proof-provenance.md')
    for required in ['source path', 'comparison window', 'attribution confidence']:
        assert required in proof


def test_subskills_reference_new_workflows():
    root = read('SKILL.md')
    seo = read('skills/seo-copywriting/SKILL.md')
    social = read('skills/social-copywriting/SKILL.md')
    french = read('skills/french-copywriting/SKILL.md')
    career = read('skills/career-copywriting/SKILL.md')
    assert 'drayton-eddie-principles.md' in root
    assert 'seo-growth-copy-integration.md' in seo
    assert 'micro-lesson-workflow.md' in social
    assert 'concision-pass.md' in french
    assert 'proof-provenance.md' in career


def test_human_voice_dash_override_present():
    text = read('references/human-voice-rules.md')
    assert 'User or brand override wins' in text
    assert 'zero em dashes and zero en dashes' in text
