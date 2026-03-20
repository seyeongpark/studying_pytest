# tests/test_fixture_yield.py

import pytest

@pytest.fixture
def file_writer():
    f = open("test.txt", "w", encoding="utf-8")
    print("\n -- File opened --")
    
    yield f  # 내가 파일을 열어서 테스트 함수에 파일 객체를 전달
    
    f.close()
    print("\n -- File closed --")
    
def test_write_sentence(file_writer):
    print("\n -- Test started --")
    text = "Hello, pytest fixture with yield!"
    file_writer.write(text)
    file_writer.flush()  # 버퍼에 있는 내용을 파일에 기록
    print("\n -- Test finished --")
    
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
        
        assert text in content