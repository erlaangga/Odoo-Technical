from openerp.osv import osv,fields

class Pelajaran(osv.osv):
    _name = "data.pelajaran"
    
    _columns = {
                "name":fields.char("Nama"),
                "id_pelajaran":fields.char("ID Pelajaran",size=10)
                }