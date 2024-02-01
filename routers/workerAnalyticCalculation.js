const {Router} = require("express")

const router = new Router()

const workerAnalyticController = require("../Controllsers/workerAnalyticController")

router.get("/get_worker_metrics",workerAnalyticController.getWorkerMetrics)

module.exports = router