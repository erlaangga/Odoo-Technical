from openerp.osv import osv,fields

class Mahasiswa(osv.osv):
    _name = "data.mahasiswa"
    
    _columns = {
                "name":fields.char("Nama Mahasiswa"),
                "id_mahasiswa": fields.char("Kode Mahasiswa")
                }