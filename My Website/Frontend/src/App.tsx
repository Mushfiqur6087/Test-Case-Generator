import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Transfer from "./pages/Transfer";
import OpenAccount from "./pages/OpenAccount";
import BillPay from "./pages/BillPay";
import RequestLoan from "./pages/RequestLoan";
import Layout from "./components/Layout";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          {/* Public routes */}
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          
          {/* Protected routes with Layout */}
          <Route path="/dashboard" element={<Layout><Dashboard /></Layout>} />
          <Route path="/transfer" element={<Layout><Transfer /></Layout>} />
          <Route path="/open-account" element={<Layout><OpenAccount /></Layout>} />
          <Route path="/bill-pay" element={<Layout><BillPay /></Layout>} />
          <Route path="/loan" element={<Layout><RequestLoan /></Layout>} />
          <Route path="/profile" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Update Contact Info</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          <Route path="/cards" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Manage Cards</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          <Route path="/investments" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Investments</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          <Route path="/statements" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Account Statements</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          <Route path="/security" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Security Settings</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          <Route path="/support" element={<Layout><div className="text-center py-8"><h1 className="text-2xl font-bold">Support Center</h1><p className="text-muted-foreground">Coming soon...</p></div></Layout>} />
          
          {/* Catch-all route */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
