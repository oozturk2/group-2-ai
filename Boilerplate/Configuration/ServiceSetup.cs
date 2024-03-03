using Boilerplate.Domain.Repositories;
using Boilerplate.Persistence;
using Boilerplate.Persistence.Repositories;
using Boilerplate.SessionState;
using Microsoft.AspNetCore.Authentication.OpenIdConnect;
using Microsoft.EntityFrameworkCore;
using Microsoft.Identity.Web;
using Microsoft.Identity.Web.UI;
using Syncfusion.Blazor;

namespace Boilerplate.Configuration;

internal static class ServiceSetup
{
    public static IServiceCollection AddServices(this IServiceCollection services, ConfigurationManager configuration)
    {


        services.AddMicrosoftIdentityWebAppAuthentication(configuration);


        services.AddAuthorization(options =>
        {
            options.FallbackPolicy = options.DefaultPolicy;

        });




        services.AddRazorPages().AddMicrosoftIdentityUI();


        services.AddServerSideBlazor().AddMicrosoftIdentityConsentHandler();

        
        services.AddSyncfusionBlazor();

     



        services.AddScoped<SessionStateManager>();


        services.AddScoped<IRepositoryManager, RepositoryManager>();

        //Database setup
        services.AddDbContext<dk2azrboilerplatesqldbContext>(options =>
            options.UseSqlServer(configuration.GetConnectionString("DatabaseConnection")));


        //If you are using the CalcEngine.Service Nuget package uncomment the line below
        //ServicesContainerRegistration.ConfigureServices(services);


        return services;
    }
}
