using Microsoft.OpenApi.Models;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

app.UseSwagger();
app.UseSwaggerUI();

app.UseHttpsRedirection();

var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
    var forecast =  Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]
        ))
        .ToArray();
    return forecast;
})
.WithName("GetWeatherForecast");


app.MapGet("/recommendations", () =>
{
    var recommendations = new[]
    {
        new SectionRecommendation(
            "b5d0c81e-0729-4718-b5e3-c0c789ce9532",
            "dfaf4951-af28-4ada-9c7b-453630431524",
            "Sección A",
            30,
            0,
            "Lunes y Miércoles 10:00-12:00",
            DateTime.Parse("0001-01-01T00:00:00Z")
        ),
        new SectionRecommendation(
            "a1b2c3d4-5678-9101-1121-314151617181",
            "123e4567-e89b-12d3-a456-426614174000",
            "Sección B",
            25,
            5,
            "Martes y Jueves 08:00-10:00",
            DateTime.UtcNow
        )
    };
    return recommendations;
})
.WithName("GetSectionRecommendations");



app.Run();

record SectionRecommendation(
    string id,
    string subject_id,
    string name,
    int total_capacity,
    int current_capacity,
    string schedule,
    DateTime creation_date
);
record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}