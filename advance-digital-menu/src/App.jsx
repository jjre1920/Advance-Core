import React, { useState } from 'react';
import { MessageCircle, Instagram, Facebook, MapPin, Shield } from 'lucide-react';

const negocios = [
  {
    id: 1,
    nombre: "ADVANCE GLOBAL",
    color: "#00f2ff",
    redes: { wa: "https://wa.me/tu_numero", ig: "#", fb: "#", map: "#" }
  },
  {
    id: 2,
    nombre: "ELITE CONNECT",
    color: "#ffca28",
    redes: { wa: "https://wa.me/otro_numero", ig: "#", fb: "#", map: "#" }
  }
];

export default function App() {
  const [sel, setSel] = useState(negocios[0]);

  return (
    <div className="min-h-screen bg-[#050505] text-white flex flex-col items-center justify-center font-sans">
      <div className="absolute top-10 flex items-center gap-2 text-gray-500">
        <Shield size={16} />
        <span className="text-xs tracking-[0.3em] uppercase">Advance Security Node</span>
      </div>

      <div className="flex gap-12 mb-24">
        {negocios.map((n) => (
          <div key={n.id} onClick={() => setSel(n)} className="group cursor-pointer flex flex-col items-center">
            <div 
              className={`w-20 h-20 rounded-2xl border-2 transition-all duration-500 ${sel.id === n.id ? 'scale-110 border-white shadow-[0_0_20px_rgba(255,255,255,0.3)]' : 'border-gray-800 opacity-30'}`} 
              style={{ backgroundColor: n.color + '22' }}
            >
            </div>
            <p className={`mt-4 text-[10px] tracking-widest transition-opacity ${sel.id === n.id ? 'opacity-100' : 'opacity-0'}`}>{n.nombre}</p>
          </div>
        ))}
      </div>

      <div className="flex gap-8 p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-xl">
        <a href={sel.redes.wa} target="_blank" className="hover:text-green-400 transition-colors"><MessageCircle size={28} /></a>
        <a href={sel.redes.ig} target="_blank" className="hover:text-pink-400 transition-colors"><Instagram size={28} /></a>
        <a href={sel.redes.fb} target="_blank" className="hover:text-blue-400 transition-colors"><Facebook size={28} /></a>
        <a href={sel.redes.map} target="_blank" className="hover:text-red-400 transition-colors"><MapPin size={28} /></a>
      </div>

      <div className="absolute bottom-10 text-[8px] text-gray-700 uppercase tracking-tighter">
        Terminal Link Active • Education Node
      </div>
    </div>
  );
}
