from pages.web import online_evaluation_page
from pages.web import vdp_page


def test_online_evaluation():
    car_id = "u3034981"
    state_number = "А889УО18"
    vdp_page.open()
    vdp_page.open_used_vdp_page(car_id)
    online_evaluation_page.open_online_evaluation_page()
    online_evaluation_page.fill_state_number(state_number)
    online_evaluation_page.find_auto()
    online_evaluation_page.go_to_next_page()
    online_evaluation_page.check_result_no_evaluation()
