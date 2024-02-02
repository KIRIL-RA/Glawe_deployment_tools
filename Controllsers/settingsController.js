class ProductionAndShopMetricsCalculationController {
    async setTargetValue(req,res,next) {
        try {
            return res.status(200).json({
                status: "ok"
            })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new ProductionAndShopMetricsCalculationController()