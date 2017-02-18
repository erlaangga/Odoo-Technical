from openerp.osv import osv,fields

class Sesi(osv.osv):
    _name = "data.sesi"
    
    _columns = {
                "name":fields.char("Nama"),
                "dosen_id":fields.many2one("data.dosen","Dosen"),
                "pelajaran_id":fields.many2one("data.pelajaran","Pelajaran"),
                "sesi_line_ids":fields.one2many("data.sesi.line","sesi_id","Sesi Line"),
                "keterangan":fields.char("Keterangan")
                }

class SesiLine(osv.osv):
    _name = "data.sesi.line"
    
    _columns = {
                "mahasiswa_id":fields.many2one("data.mahasiswa", "Mahasiswa"),
                "sesi_id":fields.many2one("data.sesi","Sesi"),
                "keterangan":fields.char("Keterangan"),
                "kehadiran":fields.boolean("Hadir"),
                }