import React from "react";
import Head from "next/head";
import '../styles/comiclab.css';
import DemoChart from "../components/ComicLabDemoChart";
import DemoTable from "../components/ComicLabDemoTable";

const ComicLabHeader: React.FC = () => (
  <header className="border-b border-lab-border bg-lab-dark sticky top-0 z-10">
    <div className="container mx-auto px-4 py-3">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <span className="text-lab-accent font-bold text-xl">COMIC</span>
          <span className="text-lab-highlight font-bold text-xl">RESEARCH</span>
          <span className="text-xs px-2 py-1 bg-lab-panel rounded">v3.1.0</span>
        </div>
        <div className="text-xs text-gray-400">
          <span className="mr-4">Last updated: <span className="text-gray-100">2023-11-16 09:42:18 UTC</span></span>
          <span>Data source: <span className="text-gray-100">research_api/v3</span></span>
        </div>
      </div>
    </div>
  </header>
);

const ComicLabFooter: React.FC = () => (
  <footer className="border-t border-lab-border py-4 mt-8 bg-lab-panel">
    <div className="container mx-auto px-4">
      <div className="flex flex-col md:flex-row justify-between items-center text-xs text-gray-400">
        <div className="mb-2 md:mb-0"></div>
        <div></div>
      </div>
      <div className="mt-2 text-xxs text-gray-500 text-center">
        Predictive models have 87-92% accuracy on historical data | Confidence intervals at 95%
      </div>
    </div>
  </footer>
);

const ComicLab: React.FC = () => {
  return (
    <>
      <Head>
        <title>ComicLab - Advanced Research Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta charSet="UTF-8" />
      </Head>
      <body className="bg-lab-dark text-gray-300 font-mono">
        <ComicLabHeader />
        <main className="container mx-auto px-4 py-6">
          {/* Executive Analysis */}
          <section className="mb-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div className="data-panel rounded-lg p-4">
                <DemoChart />
              </div>
              <div className="data-panel rounded-lg p-4">
                <div className="text-lg font-bold mb-2">Key Metrics</div>
                <ul className="text-sm space-y-1">
                  <li>Active Users: <span className="text-lab-accent font-semibold">1,234</span></li>
                  <li>Revenue: <span className="text-lab-accent font-semibold">$12,340</span></li>
                  <li>Conversion Rate: <span className="text-lab-accent font-semibold">4.2%</span></li>
                  <li>Avg. Session: <span className="text-lab-accent font-semibold">5m 12s</span></li>
                </ul>
              </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
              <div className="data-panel rounded-lg p-3 text-center">
                <div className="text-2xl font-bold text-lab-accent">87%</div>
                <div className="text-xs mt-1">Prediction Accuracy</div>
              </div>
              <div className="data-panel rounded-lg p-3 text-center">
                <div className="text-2xl font-bold text-lab-highlight">92%</div>
                <div className="text-xs mt-1">Data Coverage</div>
              </div>
              <div className="data-panel rounded-lg p-3 text-center">
                <div className="text-2xl font-bold text-lab-accent">1.2M</div>
                <div className="text-xs mt-1">Records Analyzed</div>
              </div>
              <div className="data-panel rounded-lg p-3 text-center">
                <div className="text-2xl font-bold text-lab-highlight">5</div>
                <div className="text-xs mt-1">Active Models</div>
              </div>
            </div>
          </section>
          <hr className="section-divider" />
          {/* Deep Demographic Analysis */}
          <section className="mb-8">
            <h2 className="text-xl font-semibold mb-4">DEMOGRAPHIC DEEP DIVE</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <div className="data-panel rounded-lg p-4"></div>
              <div className="data-panel rounded-lg p-4"></div>
              <div className="data-panel rounded-lg p-4"></div>
            </div>
            <div className="data-panel rounded-lg mb-6 p-4">
              <div className="flex justify-between items-center mb-4"></div>
              <div className="grid grid-cols-1 md:grid-cols-4 gap-3"></div>
            </div>
          </section>
          <hr className="section-divider" />
          {/* Predictive Analytics */}
          <section className="mb-8">
            <h2 className="text-xl font-semibold mb-4 flex items-center">
              <span className="status-indicator bg-lab-purple"></span>
              <span>PREDICTIVE ANALYTICS</span>
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div className="data-panel rounded-lg p-4"></div>
              <div className="data-panel rounded-lg p-4"></div>
            </div>
            <div className="data-panel rounded-lg p-4">
              <div className="flex justify-between items-center mb-3"></div>
              <div className="grid grid-cols-1 md:grid-cols-4 gap-3"></div>
            </div>
          </section>
          <hr className="section-divider" />
          {/* Genre Performance Detail */}
          <section className="mb-8">
            <h2 className="text-xl font-semibold mb-4">GENRE PERFORMANCE MATRIX</h2>
            <div className="overflow-x-auto">
              <DemoTable />
            </div>
          </section>
        </main>
        <ComicLabFooter />
        <p style={{borderRadius:8, textAlign:'center', fontSize:12, color:'#fff', marginTop:16,position:'fixed', left:8, bottom:8, zIndex:10, background:'rgba(0,0,0,0.8)', padding:'4px 8px'}}>
          Made with <img src="https://enzostvs-deepsite.hf.space/logo.svg" alt="DeepSite Logo" style={{width:16, height:16, verticalAlign:'middle',display:'inline-block',marginRight:3,filter:'brightness(0) invert(1)'}} />
          <a href="https://enzostvs-deepsite.hf.space" style={{color:'#fff',textDecoration:'underline'}} target="_blank" rel="noopener noreferrer">DeepSite</a> - <a href="https://enzostvs-deepsite.hf.space?remix=nmtalhp/comic-datat" style={{color:'#fff',textDecoration:'underline'}} target="_blank" rel="noopener noreferrer">🧬 Remix</a>
        </p>
      </body>
    </>
  );
};

export default ComicLab;
