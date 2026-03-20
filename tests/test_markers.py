# tests/test_markers.py
import pytest

@pytest.mark.smoke # smoke는 빠르게 실행되는 테스트를 나타내는 마커입니다. 일반적으로 핵심 기능을 검증하는 테스트에 사용됩니다.
def test_login():
    print("Login feature test")
    assert True
    
@pytest.mark.regression # regression은 기존 기능이 새로운 변경으로 인해 영향을 받지 않는지 확인하는 테스트를 나타내는 마커입니다. 일반적으로 버그 수정 후에 해당 기능이 여전히 정상적으로 작동하는지 검증하는 테스트에 사용됩니다.
def test_old_bug_case():
    print("Checking old bug case regression")
    assert True

@pytest.mark.db # db는 데이터베이스와 관련된 테스트를 나타내는 마커입니다. 일반적으로 데이터베이스 연결, 쿼리 실행, 데이터 무결성 등을 검증하는 테스트에 사용됩니다.
def test_insert_record():
    print("DB Test")
    assert True
    
@pytest.mark.api
def test_rest_endpoint():
    print("API Test")
    assert True

@pytest.mark.slow
def test_big_model_training():
    print("Slow Test")
    assert True

@pytest.mark.fast
def test_small_function():
    print("Fast Test")
    assert True

@pytest.mark.xfail(reason="Known bug: issue #123") # xfail는 테스트가 실패할 것으로 예상되는 경우에 사용하는 마커입니다. 일반적으로 알려진 버그나 아직 해결되지 않은 문제에 대한 테스트에 사용됩니다. 이 마커가 적용된 테스트가 실패하면 테스트 결과는 "expected failure"로 표시되고, 성공하면 "unexpected success"로 표시됩니다.
def test_known_bug():
    print("Known bug test")
    assert 1 == 2
    