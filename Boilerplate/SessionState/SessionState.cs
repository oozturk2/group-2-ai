namespace Boilerplate.SessionState;

public class SessionState
{
    public SessionState(bool userIsLoggedIn, bool userIsAdmin, Guid userId, Guid randomId, string userName, string name, string language)
    {
        UserIsLoggedIn = userIsLoggedIn;
        UserIsAdmin = userIsAdmin;
        UserId = userId;
        RandomId = randomId;
        UserName = userName;
        Name = name;
        Language = language;
    }

    public bool UserIsLoggedIn { get; }
    public bool UserIsAdmin { get; }
    public Guid UserId { get; } 
    public Guid RandomId { get; }
    public string Name { get; }
    public string UserName { get; }
    public string Language { get; }


}