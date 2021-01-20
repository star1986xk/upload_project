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

 Date: 13/01/2021 17:33:04
*/


-- ----------------------------
-- Table structure for check_view
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[check_view]') AND type IN ('U'))
	DROP TABLE [dbo].[check_view]
GO

CREATE TABLE [dbo].[check_view] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [uid] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [status] tinyint  NULL
)
GO

ALTER TABLE [dbo].[check_view] SET (LOCK_ESCALATION = TABLE)
GO

EXEC sp_addextendedproperty
'MS_Description', N'0待审核，1通过，2拒绝',
'SCHEMA', N'dbo',
'TABLE', N'check_view',
'COLUMN', N'status'
GO


-- ----------------------------
-- Auto increment value for check_view
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[check_view]', RESEED, 2)
GO


-- ----------------------------
-- Primary Key structure for table check_view
-- ----------------------------
ALTER TABLE [dbo].[check_view] ADD CONSTRAINT [PK__check_vi__3213E83F17C286CF] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

