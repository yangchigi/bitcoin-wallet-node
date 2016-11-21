{
  'targets': [
    {
      'target_name': 'bdb',
      'type': 'static_library',
      'cflags': ['-fPIC'],
      'include_dirs': [
        './build_unix',
      ],
      'sources': [
        "./dist/../btree/bt_compare.c",
        "./dist/../btree/bt_compress.c",
        "./dist/../btree/bt_conv.c",
        "./dist/../btree/bt_curadj.c",
        "./dist/../btree/bt_cursor.c",
        "./dist/../btree/bt_delete.c",
        "./dist/../btree/bt_method.c",
        "./dist/../btree/bt_open.c",
        "./dist/../btree/bt_put.c",
        "./dist/../btree/bt_rec.c",
        "./dist/../btree/bt_reclaim.c",
        "./dist/../btree/bt_recno.c",
        "./dist/../btree/bt_rsearch.c",
        "./dist/../btree/bt_search.c",
        "./dist/../btree/bt_split.c",
        "./dist/../btree/bt_stat.c",
        "./dist/../btree/bt_compact.c",
        "./dist/../btree/bt_upgrade.c",
        "./dist/../btree/btree_auto.c",
        "./dist/../hash/hash_stub.c",
        "./dist/../qam/qam_stub.c",
        "./dist/../rep/rep_stub.c",
        "./dist/../repmgr/repmgr_stub.c",
        "./dist/../db/db_vrfy_stub.c",
        "./dist/../lock/lock_stub.c",
        "./dist/../mutex/mut_stub.c",
        "./dist/../common/crypto_stub.c",
        "./dist/../db/crdel_auto.c",
        "./dist/../db/crdel_rec.c",
        "./dist/../db/db.c",
        "./dist/../db/db_am.c",
        "./dist/../db/db_auto.c",
        "./dist/../common/db_byteorder.c",
        "./dist/../db/db_cam.c",
        "./dist/../db/db_cds.c",
        "./dist/../common/db_compint.c",
        "./dist/../db/db_conv.c",
        "./dist/../db/db_dispatch.c",
        "./dist/../db/db_dup.c",
        "./dist/../common/db_err.c",
        "./dist/../common/db_getlong.c",
        "./dist/../common/db_idspace.c",
        "./dist/../db/db_iface.c",
        "./dist/../db/db_join.c",
        "./dist/../common/db_log2.c",
        "./dist/../db/db_meta.c",
        "./dist/../db/db_method.c",
        "./dist/../db/db_open.c",
        "./dist/../db/db_overflow.c",
        "./dist/../db/db_pr.c",
        "./dist/../db/db_rec.c",
        "./dist/../db/db_reclaim.c",
        "./dist/../db/db_remove.c",
        "./dist/../db/db_rename.c",
        "./dist/../db/db_ret.c",
        "./dist/../db/db_setid.c",
        "./dist/../db/db_setlsn.c",
        "./dist/../common/db_shash.c",
        "./dist/../db/db_sort_multiple.c",
        "./dist/../db/db_stati.c",
        "./dist/../db/db_truncate.c",
        "./dist/../db/db_upg.c",
        "./dist/../db/db_upg_opd.c",
        "./dist/../dbm/dbm.c",
        "./dist/../dbreg/dbreg.c",
        "./dist/../dbreg/dbreg_auto.c",
        "./dist/../dbreg/dbreg_rec.c",
        "./dist/../dbreg/dbreg_stat.c",
        "./dist/../dbreg/dbreg_util.c",
        "./dist/../common/dbt.c",
        "./dist/../env/env_alloc.c",
        "./dist/../env/env_config.c",
        "./dist/../env/env_failchk.c",
        "./dist/../env/env_file.c",
        "./dist/../env/env_globals.c",
        "./dist/../env/env_method.c",
        "./dist/../env/env_name.c",
        "./dist/../env/env_open.c",
        "./dist/../env/env_recover.c",
        "./dist/../env/env_region.c",
        "./dist/../env/env_register.c",
        "./dist/../env/env_sig.c",
        "./dist/../env/env_stat.c",
        "./dist/../fileops/fileops_auto.c",
        "./dist/../fileops/fop_basic.c",
        "./dist/../fileops/fop_rec.c",
        "./dist/../fileops/fop_util.c",
        "./dist/../hash/hash_func.c",
        "./dist/../hmac/hmac.c",
        "./dist/../hsearch/hsearch.c",
        "./dist/../log/log.c",
        "./dist/../log/log_archive.c",
        "./dist/../log/log_compare.c",
        "./dist/../log/log_debug.c",
        "./dist/../log/log_get.c",
        "./dist/../log/log_method.c",
        "./dist/../log/log_put.c",
        "./dist/../log/log_stat.c",
        "./dist/../common/mkpath.c",
        "./dist/../mp/mp_alloc.c",
        "./dist/../mp/mp_bh.c",
        "./dist/../mp/mp_fget.c",
        "./dist/../mp/mp_fmethod.c",
        "./dist/../mp/mp_fopen.c",
        "./dist/../mp/mp_fput.c",
        "./dist/../mp/mp_fset.c",
        "./dist/../mp/mp_method.c",
        "./dist/../mp/mp_mvcc.c",
        "./dist/../mp/mp_region.c",
        "./dist/../mp/mp_register.c",
        "./dist/../mp/mp_resize.c",
        "./dist/../mp/mp_stat.c",
        "./dist/../mp/mp_sync.c",
        "./dist/../mp/mp_trickle.c",
        "./dist/../common/openflags.c",
        "./dist/../os/os_abort.c",
        "./dist/../os/os_abs.c",
        "./dist/../os/os_alloc.c",
        "./dist/../os/os_clock.c",
        "./dist/../os/os_cpu.c",
        "./dist/../os/os_ctime.c",
        "./dist/../os/os_config.c",
        "./dist/../os/os_dir.c",
        "./dist/../os/os_errno.c",
        "./dist/../os/os_fid.c",
        "./dist/../os/os_flock.c",
        "./dist/../os/os_fsync.c",
        "./dist/../os/os_getenv.c",
        "./dist/../os/os_handle.c",
        "./dist/../os/os_map.c",
        "./dist/../common/os_method.c",
        "./dist/../os/os_mkdir.c",
        "./dist/../os/os_open.c",
        "./dist/../os/os_pid.c",
        "./dist/../os/os_rename.c",
        "./dist/../os/os_root.c",
        "./dist/../os/os_rpath.c",
        "./dist/../os/os_rw.c",
        "./dist/../os/os_seek.c",
        "./dist/../os/os_stack.c",
        "./dist/../os/os_stat.c",
        "./dist/../os/os_tmpdir.c",
        "./dist/../os/os_truncate.c",
        "./dist/../os/os_uid.c",
        "./dist/../os/os_unlink.c",
        "./dist/../os/os_yield.c",
        "./dist/../db/partition.c",
        "./dist/../sequence/seq_stat.c",
        "./dist/../sequence/sequence.c",
        "./dist/../hmac/sha1.c",
        "./dist/../clib/snprintf.c",
        "./dist/../txn/txn.c",
        "./dist/../txn/txn_auto.c",
        "./dist/../txn/txn_chkpt.c",
        "./dist/../txn/txn_failchk.c",
        "./dist/../txn/txn_method.c",
        "./dist/../txn/txn_rec.c",
        "./dist/../txn/txn_recover.c",
        "./dist/../txn/txn_region.c",
        "./dist/../txn/txn_stat.c",
        "./dist/../txn/txn_util.c",
        "./dist/../common/zerofill.c",
        "./dist/../db_archive/db_archive.c",
        "./dist/../common/util_sig.c",
        "./dist/../db_checkpoint/db_checkpoint.c",
        "./dist/../common/util_log.c",
        "./dist/../db_deadlock/db_deadlock.c",
        "./dist/../db_dump/db_dump.c",
        "./dist/../common/util_cache.c",
        "./dist/../db_hotbackup/db_hotbackup.c",
        "./dist/../db_load/db_load.c",
        "./dist/../db_printlog/db_printlog.c",
        "./dist/../btree/btree_autop.c",
        "./dist/../db/crdel_autop.c",
        "./dist/../db/db_autop.c",
        "./dist/../dbreg/dbreg_autop.c",
        "./dist/../fileops/fileops_autop.c",
        "./dist/../hash/hash_autop.c",
        "./dist/../txn/txn_autop.c",
        "./dist/../db_recover/db_recover.c",
        "./dist/../db_sql/db_sql.c",
        "./dist/../db_sql/sqlite/parse.c",
        "./dist/../db_sql/preparser.c",
        "./dist/../db_sql/parsefuncs.c",
        "./dist/../db_sql/tokenize.c",
        "./dist/../db_sql/sqlite/sqlprintf.c",
        "./dist/../db_sql/buildpt.c",
        "./dist/../db_sql/utils.c",
        "./dist/../db_sql/generate.c",
        "./dist/../db_sql/generate_test.c",
        "./dist/../db_sql/generation_utils.c",
        "./dist/../db_sql/generate_verification.c",
        "./dist/../db_sql/hint_comment.c",
        "./dist/../db_stat/db_stat.c",
        "./dist/../db_upgrade/db_upgrade.c",
        "./dist/../db_verify/db_verify.c"
      ],
      'conditions': [
        ['OS=="linux"', 
          {
            'defines': [
              '_GNU_SOURCE',
              '_REENTRANT',
              'PIC'
            ],
            'include_dirs': [
              'build_unix',
              '.',
            ]
          }
        ]
      ]
    }
  ]
}
