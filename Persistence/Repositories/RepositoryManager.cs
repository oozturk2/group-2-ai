using Boilerplate.Domain.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Boilerplate.Persistence.Repositories;
public sealed class RepositoryManager : IRepositoryManager
{
    private readonly Lazy<IColRepo> _colRepo;

    public RepositoryManager(dk2azrboilerplatesqldbContext dk2AzrboilerplatesqldbContext)
    {
        _colRepo = new Lazy<IColRepo>(() => new ColRepo(dk2AzrboilerplatesqldbContext));
    }

    public IColRepo ColRepo => _colRepo.Value;
}
