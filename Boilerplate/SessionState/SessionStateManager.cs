using System.Security.Claims;
using Microsoft.AspNetCore.Components.Authorization;
using Microsoft.AspNetCore.Components.Server.ProtectedBrowserStorage;

namespace Boilerplate.SessionState;

internal class SessionStateManager
{
    private readonly ProtectedSessionStorage _protectedSessionStorage;
    private readonly AuthenticationStateProvider _authenticationStateProvider;

    public SessionStateManager(ProtectedSessionStorage protectedSessionStorage,
        AuthenticationStateProvider authenticationStateProvider)
    {
        _protectedSessionStorage = protectedSessionStorage;
        _authenticationStateProvider = authenticationStateProvider;
    }

    #region Get Values

    internal async Task<SessionState> GetSessionState()
    {
        const string notLoggedInText = "User is not logged in";
        var loggedIn = false;

        var user = await GetCurrentUser();
        if (user.Identity is { IsAuthenticated: true })
            loggedIn = true;


        var oid = user.Claims.SingleOrDefault(e =>
            e.Type.Equals("http://schemas.microsoft.com/identity/claims/objectidentifier"));
        var objectIdentifier = oid != null ? Guid.Parse(oid.Value) : Guid.Empty;
        var userName = user.Claims.SingleOrDefault(e => e.Type.Equals("preferred_username"))?.Value ?? notLoggedInText;
        var name = user.Claims.SingleOrDefault(e => e.Type.Equals("name"))?.Value ?? notLoggedInText;

        return new SessionState(loggedIn, await IsAdmin(), objectIdentifier, await GetCurrentRandomId(), userName, name,
            await GetCurrentLanguage());
    }


    private async Task<bool> IsAdmin()
    {
        var isAdmin = await _protectedSessionStorage.GetAsync<bool>("userIsAdmin");
        return isAdmin is { Success: true, Value: true };
    }


    private async Task<Guid> GetCurrentRandomId()
    {
        var randomId = await _protectedSessionStorage.GetAsync<Guid>("randomId");
        if (randomId.Success)
        {
            return randomId.Value;
        }

        return Guid.Empty;
    }

    private async Task<string> GetCurrentLanguage()
    {
        var language = await _protectedSessionStorage.GetAsync<string>("language");
        if (language.Success)
        {
            return language.Value;
        }
        return string.Empty;
    }

    #endregion


    #region Set Values

    public void AdminLogin()
    {
        _protectedSessionStorage.SetAsync("userIsAdmin", true);
        NotifyStateChanged();
    }

    public void AdminLogout()
    {
        _protectedSessionStorage.SetAsync("userIsAdmin", false);
        NotifyStateChanged();
    }


    public void SetCurrentRandomId(Guid randomId)
    {
        _protectedSessionStorage.SetAsync("randomId", randomId);
        NotifyStateChanged();
    }

    public void SetCurrentLanguage(string language)
    {
        _protectedSessionStorage.SetAsync("language", language);
        NotifyStateChanged();
    }

    #endregion


    private async Task<ClaimsPrincipal> GetCurrentUser()
    {
        var authState = await _authenticationStateProvider.GetAuthenticationStateAsync();
        return authState.User;
    }


    public event Action? OnChange;
    private void NotifyStateChanged() => OnChange?.Invoke();
}