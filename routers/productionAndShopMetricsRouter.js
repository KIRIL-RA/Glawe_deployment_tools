const {Router} = require("express")

const router = new Router()


const productionAndShopMetricsCalculationController = require("../Controllsers/productionAndShopMetricsCalculationController")

router.get("/get_production_metrics",productionAndShopMetricsCalculationController.getProductionMetrics)
router.get("/get_shop_metrics",productionAndShopMetricsCalculationController.getShopMetrics)

module.exports = router