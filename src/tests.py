from load import get_api_data

def test_api_data():
    df = get_api_data()

    assert df is not None
    assert not df.empty
    assert "userId" in df.columns
    assert "id" in df.columns
    assert "title" in df.columns
    assert "body" in df.columns