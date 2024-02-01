const {Router} = require("express")

const router = new Router()


const consolidationController = require("../Controllsers/consolidationController")

router.post("/get_formatted_data",consolidationController.getFormattedMetrics)
router.get("/get_available_metrics",consolidationController.getAvailableMetrics)

module.exports = router