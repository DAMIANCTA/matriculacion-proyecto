
using HotChocolate;
using HotChocolate.Types;
using ai_recommender_service.Services;

public class Query
{
    public string GenerateRecommendations([Service] RecommenderService recommender, string userId)
    {
        return recommender.GetRecommendations(userId);
    }
}
