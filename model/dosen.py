from openerp.osv import fields, osv

class Dosen(osv.osv):
    _name="data.dosen"
    
    _columns = {
                "name":fields.char("Nama Dosen"),
                "id_dosen":fields.char("ID Dosen")
                }   
    