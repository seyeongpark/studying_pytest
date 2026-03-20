# tests/test_fixture_scope.py

import pytest

# scope="session" : 테스트 세션 전체에서 하나의 인스턴스를 공유
# scope="module" : 하나의 모듈 내에서 하나의 인스턴스를
# scope="class" : 하나의 클래스 내에서 하나의 인스턴스를
# scope="function" : 각 테스트 함수마다 새로운 인스턴스를 생성 (기본값)
# scope="package" : 하나의 패키지 내에서 하나의 인스턴스를 생성 (pytest 7.0 이상에서 지원)

@pytest.fixture(scope="function")
def sample_data():
    print("\n ----- data load -----")
    data = {"id": 1, "name": "SPARK"}
    return data

class TestUser:
    def test_id(self, sample_data):
        assert sample_data["id"] == 1
        
    def test_name(self, sample_data):
        assert sample_data["name"] == "SPARK"
        
class TestGuest:
    def test_id(self, sample_data):
        assert sample_data["id"] == 1