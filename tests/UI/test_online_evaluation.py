from pages.web.online_evaluation_page import OnlineEvaluationPage
from pages.web.vdp_page import CarPage


def test_online_evaluation():
    car_page = CarPage()
    OnlineEvaluation = OnlineEvaluationPage()
    car_id = "u3002728"
    state_number = "А889УО18"
    car_page.open()
    car_page.open_used_vdp_page(car_id)
    OnlineEvaluation.open_online_evaluation_page()
    OnlineEvaluation.fill_state_number(state_number)
    OnlineEvaluation.find_auto()
    OnlineEvaluation.go_to_next_page()
    OnlineEvaluation.check_result_no_evaluation()
