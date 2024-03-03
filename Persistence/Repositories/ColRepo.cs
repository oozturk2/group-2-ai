using Boilerplate.Domain;
using Boilerplate.Domain.Repositories;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Boilerplate.Persistence.Repositories;
internal sealed class ColRepo : IColRepo
{
    private readonly dk2azrboilerplatesqldbContext _context;

    public ColRepo(dk2azrboilerplatesqldbContext context)
    {
        _context = context;
    }

    public async Task<List<ColTest>> GetAllAsync(CancellationToken cancellationToken = default)
    {
        return await _context.ColTest.AsNoTracking().ToListAsync(cancellationToken);
    }
}
