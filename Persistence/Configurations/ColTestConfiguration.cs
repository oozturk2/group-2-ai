﻿// <auto-generated> This file has been auto generated by EF Core Power Tools. </auto-generated>
using Boilerplate.Domain;
using Boilerplate.Persistence;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using System;
using System.Collections.Generic;

namespace Boilerplate.Persistence.Configurations
{
    public partial class ColTestConfiguration : IEntityTypeConfiguration<ColTest>
    {
        public void Configure(EntityTypeBuilder<ColTest> entity)
        {
            entity.HasKey(e => e.RecordId);

            entity.ToTable("colTest");

            entity.Property(e => e.RecordId)
                .HasColumnName("RecordID")
                .HasDefaultValueSql("(newid())");

            entity.Property(e => e.ColBoolean).HasColumnName("colBoolean");

            entity.Property(e => e.ColInt).HasColumnName("colInt");

            entity.Property(e => e.ColNumeric)
                .HasColumnType("numeric(18, 4)")
                .HasColumnName("colNumeric");

            entity.Property(e => e.ColString1)
                .HasMaxLength(50)
                .HasColumnName("colString1");

            entity.Property(e => e.ColString2)
                .HasMaxLength(50)
                .HasColumnName("colString2");

            OnConfigurePartial(entity);
        }

        partial void OnConfigurePartial(EntityTypeBuilder<ColTest> entity);
    }
}
