﻿// <auto-generated> This file has been auto generated by EF Core Power Tools. </auto-generated>
using Boilerplate.Domain;
using Boilerplate.Persistence.Configurations;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using System;
using System.Collections.Generic;
#nullable disable

namespace Boilerplate.Persistence
{
    public partial class dk2azrboilerplatesqldbContext : DbContext
    {
        public dk2azrboilerplatesqldbContext()
        {
        }

        public dk2azrboilerplatesqldbContext(DbContextOptions<dk2azrboilerplatesqldbContext> options)
            : base(options)
        {
        }

        public virtual DbSet<ColTest> ColTest { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new Configurations.ColTestConfiguration());

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
