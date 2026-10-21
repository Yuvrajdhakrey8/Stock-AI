import React, { useState } from 'react';

interface CompanyLogoProps {
  name: string;
  symbol?: string;
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

// Curated domain mapping for top Indian stocks & IPOs for instant logo resolution
const BRAND_DOMAINS: Record<string, string> = {
  // Top Stocks
  'RELIANCE': 'ril.com',
  'TCS': 'tcs.com',
  'HDFCBANK': 'hdfcbank.com',
  'INFY': 'infosys.com',
  'ICICIBANK': 'icicibank.com',
  'TATAMOTORS': 'tatamotors.com',
  'TATASTEEL': 'tatasteel.com',
  'SBIN': 'sbi.co.in',
  'BHARTIARTL': 'airtel.in',
  'ITC': 'itcportal.com',
  'KOTAKBANK': 'kotak.com',
  'LT': 'larsentoubro.com',
  'AXISBANK': 'axisbank.com',
  'HINDUNILVR': 'hul.co.in',
  'MARUTI': 'marutisuzuki.com',
  'BAJFINANCE': 'bajajfinserv.in',
  'ASIANPAINT': 'asianpaints.com',
  'MUTHOOTFIN': 'muthootfinance.com',
  'ETERNAL': 'zomato.com',
  'ZOMATO': 'zomato.com',
  'PAYTM': 'paytm.com',
  'NYKAA': 'nykaa.com',
  'HAL': 'hal-india.co.in',
  'TITAN': 'titancompany.in',
  'WIPRO': 'wipro.com',
  'ADANIENT': 'adanienterprises.com',
  'ADANIPORTS': 'adaniports.com',
  'SUNPHARMA': 'sunpharma.com',
  'POWERGRID': 'powergrid.in',
  'NTPC': 'ntpc.co.in',
  'ONGC': 'ongcindia.com',
  'COALINDIA': 'coalindia.in',
  'IRCTC': 'irctc.co.in',
  'BHEL': 'bhel.com',
  'BEL': 'bel-india.in',
  'TECHM': 'techmahindra.com',
  'ULTRACEMCO': 'ultratechcement.com',
  'HCLTECH': 'hcltech.com',
  'LTTS': 'ltts.com',
  'TRENT': 'mytrent.com',
  'PCJEWELLER': 'pcjeweller.com',
  'FRACTAL': 'fractal.ai',
  'SHOPERSTOP': 'shoppersstop.com',

  // Prominent IPOs
  'JIO': 'jio.com',
  'PARAS': 'parashospitals.com',
  'ZETWERK': 'zetwerk.com',
  'TONBO': 'tonboimaging.com',
  'SAHAJANAND': 'smtpl.com',
  'SMT': 'smtpl.com',
  'SHELLZ': 'shellz.in',
  'BONFIGLIOLI': 'bonfiglioli.com',
  'RAVITA': 'ravitaengineering.com',
  'FUSION': 'fusioncx.com',
  'SWIGGY': 'swiggy.com',
  'HYUNDAI': 'hyundai.com',
  'OLAELEC': 'olaelectric.com',
  'BAJAJHFL': 'bajajhousingfinance.in',
  'PREMIEREN': 'premierenergies.com',
  'KRN': 'krnheat-exchanger.com',
  'WAREE': 'waaree.com',
  'AFFELE': 'affle.com',
  'ACME': 'acme.in',
  'SAGAR': 'sagardeep.org',
  'DIFFUSION': 'diffusionengineers.com',
  'MANBA': 'manbafinance.com',
  'ARKADE': 'arkade.in',
  'NORTHERN': 'northernarc.com',
  'WESTERN': 'westerncarriers.in',
  'TOLINS': 'tolinstyres.com',
  'KROSS': 'krosslimited.com',
  'GALA': 'galaprecision.com',
  'BAAZAR': 'baazarstyle.com',
  'ECOS': 'ecosmobility.com',
  'ORIENT': 'orienttech.com',
  'INTERARCH': 'interarchbuildings.com',
  'SARASWATI': 'ssilindia.com',
};

// Groww-style vibrant color palettes for fallback monogram badges
const VIBRANT_PALETTES = [
  { bg: 'bg-amber-500', text: 'text-slate-950', ring: 'ring-amber-400/30' },
  { bg: 'bg-blue-600', text: 'text-white', ring: 'ring-blue-400/30' },
  { bg: 'bg-emerald-600', text: 'text-white', ring: 'ring-emerald-400/30' },
  { bg: 'bg-purple-600', text: 'text-white', ring: 'ring-purple-400/30' },
  { bg: 'bg-rose-500', text: 'text-white', ring: 'ring-rose-400/30' },
  { bg: 'bg-indigo-600', text: 'text-white', ring: 'ring-indigo-400/30' },
  { bg: 'bg-teal-500', text: 'text-slate-950', ring: 'ring-teal-400/30' },
  { bg: 'bg-orange-500', text: 'text-white', ring: 'ring-orange-400/30' },
  { bg: 'bg-sky-500', text: 'text-slate-950', ring: 'ring-sky-400/30' },
  { bg: 'bg-pink-600', text: 'text-white', ring: 'ring-pink-400/30' },
];

function getInitials(name: string): string {
  if (!name) return 'ST';
  const clean = name
    .replace(/(Limited|Ltd|India|Corp|Technologies|Tech|Industries|Services|Finance|Enterprises|\.NS|\.BO)/gi, '')
    .trim();
  const words = clean.split(/\s+/).filter(Boolean);
  if (words.length >= 2) {
    return (words[0][0] + words[1][0]).toUpperCase();
  }
  if (words.length === 1 && words[0].length >= 2) {
    return words[0].slice(0, 3).toUpperCase();
  }
  return name.slice(0, 2).toUpperCase();
}

function getPalette(name: string) {
  let hash = 0;
  for (let i = 0; i < name.length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash);
  }
  const index = Math.abs(hash) % VIBRANT_PALETTES.length;
  return VIBRANT_PALETTES[index];
}

function getDomain(name: string, symbol?: string): string | null {
  const cleanSym = (symbol || '').replace(/\.(NS|BO)$/i, '').toUpperCase();
  if (cleanSym && BRAND_DOMAINS[cleanSym]) {
    return BRAND_DOMAINS[cleanSym];
  }

  const cleanName = name.toUpperCase();
  for (const [key, domain] of Object.entries(BRAND_DOMAINS)) {
    if (cleanName.includes(key)) {
      return domain;
    }
  }
  return null;
}

const SIZE_CLASSES = {
  xs: 'w-6 h-6 text-[10px] rounded-lg',
  sm: 'w-8 h-8 text-xs rounded-xl',
  md: 'w-10 h-10 text-sm rounded-xl',
  lg: 'w-12 h-12 text-base rounded-2xl',
  xl: 'w-14 h-14 text-lg rounded-2xl',
};

export const CompanyLogo: React.FC<CompanyLogoProps> = ({
  name,
  symbol,
  size = 'md',
  className = '',
}) => {
  const [imgFailed, setImgFailed] = useState<boolean>(false);
  const domain = getDomain(name, symbol);
  const initials = getInitials(name);
  const palette = getPalette(name);
  const sizeClass = SIZE_CLASSES[size] || SIZE_CLASSES.md;

  // Google Favicon High-Res URL
  const logoUrl = domain && !imgFailed
    ? `https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://${domain}&size=128`
    : null;

  if (logoUrl) {
    return (
      <div
        className={`relative shrink-0 flex items-center justify-center bg-white border border-slate-700/80 p-1.5 shadow-sm overflow-hidden ${sizeClass} ${className}`}
      >
        <img
          src={logoUrl}
          alt={name}
          loading="lazy"
          className="w-full h-full object-contain"
          onError={() => setImgFailed(true)}
        />
      </div>
    );
  }

  // Fallback to Groww-style vibrant initial avatar
  return (
    <div
      className={`shrink-0 flex items-center justify-center font-black tracking-tight select-none shadow-sm ring-1 ${palette.bg} ${palette.text} ${palette.ring} ${sizeClass} ${className}`}
      title={name}
    >
      <span>{initials}</span>
    </div>
  );
};
