using ai_recommender_service.GraphQL.Queries;
using ai_recommender_service.GraphQL.Types;
using ai_recommender_service.Services;
using Microsoft.AspNetCore.Server.Kestrel.Core;
using MongoDB.Driver;
using HotChocolate.AspNetCore;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<IMongoClient>(sp =>
    new MongoClient(builder.Configuration.GetConnectionString("MongoDb")));
builder.Services.AddScoped<RecommendationService>();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services
    .AddGraphQLServer()
    .AddQueryType<RecommendationQuery>()
    .AddType<RecommendationType>();

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();

app.MapGraphQL("/graphql");

app.Run();