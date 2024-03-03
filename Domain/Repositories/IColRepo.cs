using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Boilerplate.Domain.Repositories;
public interface IColRepo
{
    Task<List<ColTest>> GetAllAsync(CancellationToken cancellationToken = default);
}
