
using MongoDB.Driver;
using ai_recommender_service.Models;

namespace ai_recommender_service.Services
{
    public class RecommenderService
    {
        private readonly IMongoCollection<Recommendation> _collection;

        public RecommenderService(IConfiguration config)
        {
            var client = new MongoClient(config["MONGO_URI"]);
            var database = client.GetDatabase("recommender_ai");
            _collection = database.GetCollection<Recommendation>("ai_recommender");
        }

        public string GetRecommendations(string userId)
        {
            // Ejemplo: retornar texto simulado
            return $"Recomendaciones generadas para el usuario {userId}.";
        }
    }
}
