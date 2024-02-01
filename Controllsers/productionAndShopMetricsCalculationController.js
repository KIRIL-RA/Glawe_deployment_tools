
class ProductionAndShopMetricsCalculationController {
    async getProductionMetrics(req,res,next) {
        try {
            res.status(200).json({
                productionName: "good production",
                metrics : [
                    {
                        name: "oee",
                        type: "sometype",
                        target_value: "234",
                        units_of_measurement : "km",
                        value : 123,
                        time_start: new Date(),
                        time_end: new Date()
                    },
                    {
                        name: "kpe",
                        type: "sometype",
                        target_value: "234",
                        units_of_measurement : "km",
                        value : 123,
                        time_start: new Date(),
                        time_end: new Date()
                    },

                ]
        })
        } catch (error) {
            console.log(error);
        }
    }

    async getShopMetrics(req,res,next) {
        try {
            return res.status(200).json({
                shopName: "best shop",
                metrics : [
                    {
                        name: "oee",
                        type: "sometype",
                        units_of_measurement : "mm",
                        value : 10,
                        time_start: new Date(),
                        time_end: new Date()
                    },
                    {
                        name: "kpe",
                        type: "sometype",
                        units_of_measurement : "mm",
                        value : 10,
                        time_start: new Date(),
                        time_end: new Date()
                    },
                ]

        })
        } catch (error) {
            console.log(error);
        }
    }
}

module.exports = new ProductionAndShopMetricsCalculationController()