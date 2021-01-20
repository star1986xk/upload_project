/*
 Navicat Premium Data Transfer

 Source Server         : SQLserver单位服务器
 Source Server Type    : SQL Server
 Source Server Version : 10506000
 Source Host           : 101.200.47.16:1433
 Source Catalog        : test
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 10506000
 File Encoding         : 65001

 Date: 13/01/2021 17:34:28
*/


-- ----------------------------
-- Table structure for project_view
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[project_view]') AND type IN ('U'))
	DROP TABLE [dbo].[project_view]
GO

CREATE TABLE [dbo].[project_view] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [project_date] date  NULL,
  [name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[project_view] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Auto increment value for project_view
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[project_view]', RESEED, 2)
GO


-- ----------------------------
-- Primary Key structure for table project_view
-- ----------------------------
ALTER TABLE [dbo].[project_view] ADD CONSTRAINT [PK__project__3213E83F03BB8E22] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

