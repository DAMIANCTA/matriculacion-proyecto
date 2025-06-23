
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace ai_recommender_service.Models
{
    public class Recommendation
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string _id { get; set; }

        [BsonElement("user_id")]
        public string UserId { get; set; }

        [BsonElement("generation_date")]
        public DateTime GenerationDate { get; set; }

        [BsonElement("recommendations")]
        public string[] Recommendations { get; set; }
    }
}
