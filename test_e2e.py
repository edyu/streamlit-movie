from streamlit.testing.v1 import AppTest

def test_movie_search_end_to_end():
    at = AppTest.from_file("frontend.py")
    at.run()

    assert len(at.sidebar.text_input) == 1
    assert len(at.sidebar.button) == 1

    at.sidebar.text_input[0].set_value("Inception").run()
    at.sidebar.button[0].click().run()

    assert "results" in at.session_state
    results = at.session_state["results"]

    assert len(results) > 0

    assert len(at.expander) == len(results)

    for idx, movie in enumerate(results.values()):
        title = movie["title"]
        assert title in at.expander[idx].label

        overview_text = f"**Overview:** {movie.get('overview', 'N/A')}"
        assert any(overview_text in m.value for m in at.markdown), \
                f"Overview for {title} not found"
